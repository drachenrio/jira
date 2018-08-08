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
url="http://localhost:2990/jira/rest/api/2/issue/JI-1"

response=requests.get(url, auth=("j*.l*o", "W*123!"))
data=response.json()
pprint.pprint(data)
