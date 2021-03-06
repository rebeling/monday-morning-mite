from secrets import MITE_URL, MITE_API_KEY, USERS
from requests import get
from utils import user_entry, user_statistics, tasks_per_day
from redmine import augment_from_notes

HEADERS = {'X-MiteApiKey': MITE_API_KEY, 'Content-Type': 'application/json'}


def get_user(headers=HEADERS, mite_url=MITE_URL):
    url = '{}/users.json'.format(mite_url)
    return get(url, headers=headers).json()


def data_of_mite(at='last_week', headers=HEADERS):
    users = {}
    time_entries_url = '{}/time_entries.json?user_id={}&at=%s' % at
    for x in get_user():
        name = x['user']['name']
        if name in USERS:
            uid = x['user']['id']
            url = time_entries_url.format(MITE_URL, uid)
            entries = [user_entry(e) for e in get(url, headers=headers).json()]
            entries = augment_from_notes(entries)

            statistics = user_statistics(entries)
            users[name] = {
                'id': uid,
                'entries': entries,
                'statistics': statistics,
                'week': tasks_per_day(entries)
            }
    return users
