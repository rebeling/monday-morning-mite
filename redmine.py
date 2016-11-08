from secrets import REDMINE_URL, X_REDMINE_API_KEY
from requests import get


def augment_from_notes(entries, redmine_url=REDMINE_URL):
    """Get story points from redmine

    * done percentage
    * ticket status
    * participants - more than x people!

    * story break down is important!
    ** use tasks only and warn if something is to big to be true

    """
    augmented_entries = []
    for e in entries:

        redmine_issues = []
        splitted = e['note'].split()

        hashtagids = [x for x in splitted if '#' in x]
        if hashtagids:
            for hid in hashtagids:
                issue = get_redmine_issue_by_id(hid.replace('#', ''))
                if issue:
                    redmine_issues.append(issue)

        urlids = [x for x in splitted if redmine_url in x]
        if urlids:
            for uid in urlids:
                issue = get_redmine_issue_by_id(uid.split('/')[-1])
                if issue:
                    redmine_issues.append(issue)

        if redmine_issues:
            e['redmine_issues'] = redmine_issues

        augmented_entries.append(e)
    return augmented_entries


def get_redmine_issue_by_id(id,
                            redmine_url=REDMINE_URL,
                            redmine_key=X_REDMINE_API_KEY):
    """
    >>> get_redmine_issue_by_id('123456789')
    404
    """
    url = '{}/issues/{}.json'.format(redmine_url, id)
    r = get(url, headers={'X-Redmine-API-Key': redmine_key})
    if r.status_code == 200:
        issue = r.json()['issue']
        keys = ['id', 'subject', 'tracker', 'custom_fields', 'status']
        return {k: issue[k] for k in keys}
    else:
        print r.status_code
        return None


if __name__ == '__main__':
    entries = [
        {'note': '#9704 sth'},
        {'note': '{}/issues/11331 sth'.format(REDMINE_URL)}]
    augmented_entries = augment_from_notes(entries)
    # print augmented_entries
    # print len(augmented_entries)

    import doctest
    doctest.testmod()
