from collections import Counter
from dateutil import parser


def tasks_per_day(entries):
    week = {}
    for e in entries:
        day = week.get(e['day'], [])
        day.append(e)
        week[e['day']] = day
    return week


def user_statistics(entries):
    """Calculate all stats for one user over the entries.

    * references = Counter([x['reference'] for x in entries])
    * billable = Counter([x['billable'] for x in entries])
    * projects = Counter([x['project_name'] for x in entries]).most_common(),
    * tasks = Counter([x['service_name'][0] for x in entries])
    * times total = sum([int(x['minutes']) for x in entries])
    * mean time per entry = mean([int(x['minutes']) for x in entries])
    * mean time per day
    """
    def count(key, entries=entries):
        return Counter([x[key] for x in entries]).most_common()

    minutes = [int(x['minutes']) for x in entries]
    return {
        'references': count('reference'),
        'billable': count('billable'),
        'projects': count('project_name'),
        'tasks': count('service_name'),
        'time total': sum(minutes)/60,
        'mean per entry': (sum(minutes)/(len(entries)))/60.,
        'longest entry': max(minutes)/60,
        'shortest entry': min(minutes)/60,
        'different projects': len(count('project_name')),
        'total entries': len(entries)
    }


def user_entry(e):
    """Preprocess time entries.

    [u'user_id', u'customer_id', u'locked', u'customer_name', u'revenue',
     u'project_name', u'user_name', u'created_at', u'updated_at', u'note',
     u'date_at', u'service_name', u'billable', u'service_id', u'project_id',
     u'minutes', u'id', u'hourly_rate']
    {u'user_id': 87053, u'customer_id': 186291, u'locked': False,
     u'customer_name': u'Retresco', u'revenue': 0.0, u'project_name':
     u'RTR :: Intern_2016', u'user_name': u'X Y', u'created_at':
     u'2016-10-28T20:51:39+02:00', u'updated_at': u'2016-10-28T20:51:39+02:00',
     u'note': u'weekly', u'date_at': u'2016-10-24', u'service_name':
     u'RTR intern', u'billable': False, u'service_id': 203602, u'project_id':
     1760754, u'minutes': 30, u'id': 45795900, u'hourly_rate': 0}
    """
    time_entry = e['time_entry']
    note = time_entry['note']
    return {
        'reference': '#' in note or 'http://' in note,
        'note': note,
        'minutes': time_entry['minutes'],
        'project_name': time_entry['project_name'],
        'project_id': time_entry['project_id'],
        'date_at': time_entry['date_at'],
        'day': parser.parse(time_entry['date_at']).strftime("%A"),
        'billable': time_entry['billable'],
        'service_name': time_entry['service_name'],
        'service_id': time_entry['service_id']
    }
