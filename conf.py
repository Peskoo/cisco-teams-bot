import json


# Open secrets.json
with open('secrets.json', 'r') as f:
    data = f.read()
secrets = json.loads(data)

GITLAB_ACCESS_TOKEN = secrets['gitlab']
GITLAB_PROJECT_ID = 218
GITLAB_URL = secrets['url']
GITLAB_PROJECT_URL = f'{GITLAB_URL}/api/v4/projects/{GITLAB_PROJECT_ID}/'

NGROK_CLIENT_API_BASE_URL = 'http://localhost:4040/api'

MEMBERS = {
    'francois.rabanel': 156
}

WEBEX_TEAMS_ACCESS_TOKEN = secrets['webex']
