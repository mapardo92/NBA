#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from nba_api.stats.endpoints import shotchartdetail
import json
import pandas as pd

response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2023-24',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='Regular Season'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2023-24.csv', index=False)

