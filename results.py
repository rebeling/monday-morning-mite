
def overview(users, notes=False):

    for i, u in enumerate(users):
        print '{}. {}\n{}'.format(i, u, '-'*79)

        stats = users[u]['statistics']

        for k in ['total entries', 'tasks', 'billable', 'references',
                  'time total', 'mean per entry', 'shortest entry',
                  'longest entry', 'different projects', 'projects']:
            v = stats[k]
            if isinstance(v, list) and len(v) > 3:
                print '{}:'.format(k)
                for w in v:
                    print '  {}'.format(w)
            else:
                print '{}: {}'.format(k, v)

        if notes:
            print '\nNotes:'
            for e in users[u]['entries']:
                print '  * {}'.format(e['note'].encode('utf-8'))
            print '\n'

        weekly(users[u]['week'])


def weekly(week):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for day in weekdays:
        print "\n{}:".format(day)
        for i, e in enumerate(week[day]):
            print "  {}. {}".format(i+1, e['note'])
