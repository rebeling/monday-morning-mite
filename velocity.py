

def velocity(estimate, actual, times=60):
    """Calculate velocity.

    >>> velocity(2, 160, times=60)
    0.75
    >>> velocity(3, 160, times=60)
    1.125
    >>> velocity(3, 160, times=80)
    1.5
    """
    return (estimate*times)/(actual*1.)


def correlations(user_data):
    """Iterate entries, collect tasks by id and calculate velocity.

    >>> x = {u'Matthias Rebel': {'week': {'Tuesday': [{'note': u'joblib, parallel processing', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': True, 'service_name': u'Research', 'service_id': 362870, 'project_id': 1760754, 'minutes': 0, 'date_at': u'2016-11-01', 'day': 'Tuesday'}, {'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11333, u'Task', u'2')], 'day': 'Tuesday', 'note': u'#11333 push links to fcms', 'date_at': u'2016-11-01', 'billable': True, 'service_id': 203451, 'project_id': 1760745, 'minutes': 52}, {'project_name': u'609 :: kurier.at :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11173, u'Story', u'13')], 'day': 'Tuesday', 'note': u'#11173 content api', 'date_at': u'2016-11-01', 'billable': True, 'service_id': 203451, 'project_id': 1858590, 'minutes': 150}, {'project_name': u'665 :: DAZ :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11439, u'Task', u'3')], 'day': 'Tuesday', 'note': u'#11439 daz dump importer', 'date_at': u'2016-11-01', 'billable': True, 'service_id': 203451, 'project_id': 1975303, 'minutes': 103}], 'Friday': [{'note': u'ling analysis', 'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1760745, 'minutes': 60, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'note': u'daz deployment', 'project_name': u'665 :: DAZ :: TMS', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1975303, 'minutes': 60, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'note': u'QA and bug reports', 'project_name': u'600 & 627 :: NZZ :: TMS & TMS "Lifestyle"', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1794510, 'minutes': 30, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'note': u'Hackathon eval', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': False, 'service_name': u'RTR intern', 'service_id': 203602, 'project_id': 1760754, 'minutes': 120, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'project_name': u'RTR :: Demos 2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11418, u'Story', u'5')], 'day': 'Friday', 'note': u'#11418 initial dump enrichment and import', 'date_at': u'2016-11-04', 'billable': True, 'service_id': 203451, 'project_id': 1915553, 'minutes': 60}], 'Monday': [{'note': u'Adaptive recommendations', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': True, 'service_name': u'Research', 'service_id': 362870, 'project_id': 1760754, 'minutes': 0, 'date_at': u'2016-10-31', 'day': 'Monday'}, {'project_name': u'665 :: DAZ :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11155, u'Story', u''), (11155, u'Story', u'')], 'day': 'Monday', 'note': u'#11155 https://redmine.rtrsupport.de/issues/11155', 'date_at': u'2016-10-31', 'billable': True, 'service_id': 203451, 'project_id': 1975303, 'minutes': 30}, {'project_name': u'609 :: kurier.at :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11173, u'Story', u'13')], 'day': 'Monday', 'note': u'#11173 content api', 'date_at': u'2016-10-31', 'billable': True, 'service_id': 203451, 'project_id': 1858590, 'minutes': 120}, {'project_name': u'665 :: DAZ :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11439, u'Task', u'3'), (11439, u'Task', u'3')], 'day': 'Monday', 'note': u'#11439 dump indizieren https://redmine.rtrsupport.de/issues/11439', 'date_at': u'2016-10-31', 'billable': True, 'service_id': 203451, 'project_id': 1975303, 'minutes': 0}], 'Wednesday': [{'note': u'Hackathon eval', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': False, 'service_name': u'RTR intern', 'service_id': 203602, 'project_id': 1760754, 'minutes': 60, 'date_at': u'2016-11-02', 'day': 'Wednesday'}, {'note': u'', 'project_name': u'633C :: FAZ :: Social Share Counts', 'reference': False, 'billable': True, 'service_name': u'Konzeption', 'service_id': 203601, 'project_id': 1997399, 'minutes': 60, 'date_at': u'2016-11-02', 'day': 'Wednesday'}, {'note': u'TMS project setup', 'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': False, 'billable': True, 'service_name': u'Kommunikation', 'service_id': 286657, 'project_id': 1760745, 'minutes': 30, 'date_at': u'2016-11-02', 'day': 'Wednesday'}, {'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11333, u'Task', u'2')], 'day': 'Wednesday', 'note': u'#11333 push links to fcms', 'date_at': u'2016-11-02', 'billable': True, 'service_id': 203451, 'project_id': 1760745, 'minutes': 60}], 'Thursday': [{'note': u'QA and fixes', 'project_name': u'600 & 627 :: NZZ :: TMS & TMS "Lifestyle"', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1794510, 'minutes': 58, 'date_at': u'2016-11-03', 'day': 'Thursday'}, {'note': u'TMS version update', 'project_name': u'600 & 627 :: NZZ :: TMS & TMS "Lifestyle"', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1794510, 'minutes': 120, 'date_at': u'2016-11-03', 'day': 'Thursday'}, {'note': u'Heatmap und Kommunikation', 'project_name': u'609 :: kurier.at :: TMS', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1858590, 'minutes': 30, 'date_at': u'2016-11-03', 'day': 'Thursday'}, {'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11333, u'Task', u'2')], 'day': 'Thursday', 'note': u'#11333 push links to fcms', 'date_at': u'2016-11-03', 'billable': True, 'service_id': 203451, 'project_id': 1760745, 'minutes': 121}]}, 'statistics': {'different projects': 7, 'tasks': [(u'Entwicklung', 15), (u'RTR intern', 2), (u'Research', 2), (u'Konzeption', 1), (u'Kommunikation', 1)], 'references': [(False, 12), (True, 9)], 'time total': 22, 'billable': [(True, 19), (False, 2)], 'mean per entry': 1.05, 'total entries': 21, 'shortest entry': 0, 'projects': [(u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 5), (u'RTR :: Intern_2016', 4), (u'665 :: DAZ :: TMS', 4), (u'609 :: kurier.at :: TMS', 3), (u'600 & 627 :: NZZ :: TMS & TMS "Lifestyle"', 3), (u'RTR :: Demos 2016', 1), (u'633C :: FAZ :: Social Share Counts', 1)], 'longest entry': 2}, 'id': 51784, 'entries': [{'note': u'ling analysis', 'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1760745, 'minutes': 60, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'note': u'daz deployment', 'project_name': u'665 :: DAZ :: TMS', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1975303, 'minutes': 60, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'note': u'QA and bug reports', 'project_name': u'600 & 627 :: NZZ :: TMS & TMS "Lifestyle"', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1794510, 'minutes': 30, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'note': u'Hackathon eval', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': False, 'service_name': u'RTR intern', 'service_id': 203602, 'project_id': 1760754, 'minutes': 120, 'date_at': u'2016-11-04', 'day': 'Friday'}, {'project_name': u'RTR :: Demos 2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11418, u'Story', u'5')], 'day': 'Friday', 'note': u'#11418 initial dump enrichment and import', 'date_at': u'2016-11-04', 'billable': True, 'service_id': 203451, 'project_id': 1915553, 'minutes': 60}, {'note': u'QA and fixes', 'project_name': u'600 & 627 :: NZZ :: TMS & TMS "Lifestyle"', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1794510, 'minutes': 58, 'date_at': u'2016-11-03', 'day': 'Thursday'}, {'note': u'TMS version update', 'project_name': u'600 & 627 :: NZZ :: TMS & TMS "Lifestyle"', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1794510, 'minutes': 120, 'date_at': u'2016-11-03', 'day': 'Thursday'}, {'note': u'Heatmap und Kommunikation', 'project_name': u'609 :: kurier.at :: TMS', 'reference': False, 'billable': True, 'service_name': u'Entwicklung', 'service_id': 203451, 'project_id': 1858590, 'minutes': 30, 'date_at': u'2016-11-03', 'day': 'Thursday'}, {'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11333, u'Task', u'2')], 'day': 'Thursday', 'note': u'#11333 push links to fcms', 'date_at': u'2016-11-03', 'billable': True, 'service_id': 203451, 'project_id': 1760745, 'minutes': 121}, {'note': u'Hackathon eval', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': False, 'service_name': u'RTR intern', 'service_id': 203602, 'project_id': 1760754, 'minutes': 60, 'date_at': u'2016-11-02', 'day': 'Wednesday'}, {'note': u'', 'project_name': u'633C :: FAZ :: Social Share Counts', 'reference': False, 'billable': True, 'service_name': u'Konzeption', 'service_id': 203601, 'project_id': 1997399, 'minutes': 60, 'date_at': u'2016-11-02', 'day': 'Wednesday'}, {'note': u'TMS project setup', 'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': False, 'billable': True, 'service_name': u'Kommunikation', 'service_id': 286657, 'project_id': 1760745, 'minutes': 30, 'date_at': u'2016-11-02', 'day': 'Wednesday'}, {'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11333, u'Task', u'2')], 'day': 'Wednesday', 'note': u'#11333 push links to fcms', 'date_at': u'2016-11-02', 'billable': True, 'service_id': 203451, 'project_id': 1760745, 'minutes': 60}, {'note': u'joblib, parallel processing', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': True, 'service_name': u'Research', 'service_id': 362870, 'project_id': 1760754, 'minutes': 0, 'date_at': u'2016-11-01', 'day': 'Tuesday'}, {'project_name': u'364A :: S\xfcdkurier :: Semantische Anreicherung und TMS_2016', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11333, u'Task', u'2')], 'day': 'Tuesday', 'note': u'#11333 push links to fcms', 'date_at': u'2016-11-01', 'billable': True, 'service_id': 203451, 'project_id': 1760745, 'minutes': 52}, {'project_name': u'609 :: kurier.at :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11173, u'Story', u'13')], 'day': 'Tuesday', 'note': u'#11173 content api', 'date_at': u'2016-11-01', 'billable': True, 'service_id': 203451, 'project_id': 1858590, 'minutes': 150}, {'project_name': u'665 :: DAZ :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11439, u'Task', u'3')], 'day': 'Tuesday', 'note': u'#11439 daz dump importer', 'date_at': u'2016-11-01', 'billable': True, 'service_id': 203451, 'project_id': 1975303, 'minutes': 103}, {'note': u'Adaptive recommendations', 'project_name': u'RTR :: Intern_2016', 'reference': False, 'billable': True, 'service_name': u'Research', 'service_id': 362870, 'project_id': 1760754, 'minutes': 0, 'date_at': u'2016-10-31', 'day': 'Monday'}, {'project_name': u'665 :: DAZ :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11155, u'Story', u''), (11155, u'Story', u'')], 'day': 'Monday', 'note': u'#11155 https://redmine.rtrsupport.de/issues/11155', 'date_at': u'2016-10-31', 'billable': True, 'service_id': 203451, 'project_id': 1975303, 'minutes': 30}, {'project_name': u'609 :: kurier.at :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11173, u'Story', u'13')], 'day': 'Monday', 'note': u'#11173 content api', 'date_at': u'2016-10-31', 'billable': True, 'service_id': 203451, 'project_id': 1858590, 'minutes': 120}, {'project_name': u'665 :: DAZ :: TMS', 'reference': True, 'service_name': u'Entwicklung', 'redmine_issues': [(11439, u'Task', u'3'), (11439, u'Task', u'3')], 'day': 'Monday', 'note': u'#11439 dump indizieren https://redmine.rtrsupport.de/issues/11439', 'date_at': u'2016-10-31', 'billable': True, 'service_id': 203451, 'project_id': 1975303, 'minutes': 0}]}}
    >>> correlations(x)
    None
    """
    data = {}
    for user in user_data:

        for entry in user_data[user]['entries']:

            print entry.keys()

            if 'redmine_issues' in entry:
                issues = entry['redmine_issues']

                print "issues", issues
                # for issue_id, task, points in issues:
                #     if points:
                #         id = data.get(issue_id, {
                #                       'task': task, 'points': points,
                #                       'minutes': []})
                #         id['minutes'] += [e['minutes']]
                #         data[issue_id] = id


    # print data
    return user_data


if __name__ == '__main__':
    import doctest
    doctest.testmod()