'''
. ~/venv/bin/activate
python3 post_query_issue.py
'''

import requests
import json
import pprint

url="http://localhost:2990/jira/rest/api/2/search?jql=key=JI-1"
url="http://localhost:2990/jira/rest/api/2/issue/JI-1"
url="http://localhost:2990/rest/api/2/issue/JI-1"
url="http://localhost:2990/jira/rest/api/2/search"

query_param={"jsql":"project=Jira Integration", "startAt":0, "maxResults":2,"fields": ["id", "key", "name", "summary", "assignee"]}

resp=requests.post(url, data=query_param, auth=("jonathan.luo", "Welcome123!"))
print(resp)
print(resp.text)
data=resp.json()
pprint.pprint(data)
