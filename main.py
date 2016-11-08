from mite_api import data_of_mite
from results import overview

# 1.  get the entries from mite, default at=last_week
# 1.1 augment the data entries, parse note for ids and urls
#     and access issue in specified source
user_data = data_of_mite()
print 'retrieved'

# 2. calculate velocity
from velocity import correlations
user_data = correlations(user_data)

# 3. prepare and show data
# overview(user_data)
