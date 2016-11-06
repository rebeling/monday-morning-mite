
def overview(users):
    for i, u in enumerate(users):
        print '{}. {}\n {}'.format(i, u, '-'*79)

        stats = users[u]['statistics']

        for k in ['total entries', 'tasks', 'billable', 'references',
                  'time total', 'mean per entry', 'shortest entry',
                  'longest entry', 'different projects', 'projects']:
            v = stats[k]
            if isinstance(v, list) and len(v) > 3:
                print '{}:'.format(k)
                for w in v:
                    print '\t{}'.format(w)
            else:
                print '{}: {}'.format(k, v)

        print '\nNotes:'
        for e in users[u]['entries']:
            print '\t* {}'.format(e['note'].encode('utf-8'))
        print '\n'
