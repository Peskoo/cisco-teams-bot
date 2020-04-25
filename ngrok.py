import requests

import conf


def get_ngrok_public_url():
    """Get the ngrok public HTTP URL from the local client API."""
    try:
        response = requests.get(
            url=conf.NGROK_CLIENT_API_BASE_URL + '/tunnels',
            headers={'content-type': 'application/json'}
        )
        response.raise_for_status()

    except requests.exceptions.RequestException:
        print('Could not connect to the ngrok client API; '
              'assuming not running.')
        return None

    else:
        for tunnel in response.json()['tunnels']:
            if tunnel.get('public_url', '').startswith('http://'):
                print('Found ngrok public HTTP URL:', tunnel['public_url'])
                return tunnel['public_url']

