import json


# Open secrets.json
with open('secrets.json', 'r') as f:
    data = f.read()
secrets = json.loads(data)

GITLAB_ACCESS_TOKEN = secrets['gitlab']
GITLAB_TINA_ID = 218
GITLAB_URL = 'https://gitlab.outscale.internal'
GITLAB_TINA_URL = f'{GITLAB_URL}/api/v4/projects/{GITLAB_TINA_ID}/'

NGROK_CLIENT_API_BASE_URL = 'http://localhost:4040/api'

TINA_MEMBERS = {
    'francois.rabanel': 156
}

WEBEX_TEAMS_ACCESS_TOKEN = secrets['webex']
