#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from nba_api.stats.endpoints import shotchartdetail
import json
import pandas as pd


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2022-23',
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
df.to_csv('nba_2022-23.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2022-23',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='PlayIn'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2022-23_playin.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2022-23',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='Playoffs'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2022-23_playoffs.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2021-22',
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
df.to_csv('nba_2021-22.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2021-22',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='PlayIn'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2021-22_playin.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2021-22',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='Playoffs'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2021-22_playoffs.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2020-21',
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
df.to_csv('nba_2020-21.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2021-22',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='PlayIn'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2021-22_playin.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2020-21',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='Playoffs'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2020-21_playoffs.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2019-20',
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
df.to_csv('nba_2019-20.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2019-20',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='PlayIn'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2019-20_playin.csv', index=False)


# In[ ]:


response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2019-20',
    context_measure_simple = 'FGA', #<-- Default is 'PTS' and will only return made shots, but we want all shot attempts
    season_type_all_star='Playoffs'
)

content = json.loads(response.get_json())

results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows, columns=headers) #<-- add the columns parameter
df.columns = headers

# write to csv file
df.to_csv('nba_2019-20_playoffs.csv', index=False)

