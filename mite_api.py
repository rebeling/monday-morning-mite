from secrets import MITE_URL, MITE_API_KEY, USERS
from requests import get
from utils import user_entry, user_statistics

HEADERS = {'X-MiteApiKey': MITE_API_KEY, 'Content-Type': 'application/json'}


def get_user(headers=HEADERS, mite_url=MITE_URL):
    # url = '{}/projects.json'
    url = '{}/users.json'.format(mite_url)
    return get(url, headers=headers).json()


def data_of_mite(headers=HEADERS):
    users = {}
    time_entries_url = '{}/time_entries.json?user_id={}&at=last_week'
    for x in get_user():
        name = x['user']['name']
        if name in USERS:
            uid = x['user']['id']
            url = time_entries_url.format(MITE_URL, uid)
            entries = [user_entry(e) for e in get(url, headers=headers).json()]
            statistics = user_statistics(entries)
            users[name] = {
                'id': uid,
                'entries': entries,
                'statistics': statistics
            }
    return users
