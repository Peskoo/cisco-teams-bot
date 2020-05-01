"""Bot for webex cisco teams.

Setup before launch this file:
ngrok http 8080

Our webhooks need to hit the machine to work, but here we use localhost.
Ngrok is here to open our localhost to the world.

Flask works in local too.

- To configure server, just squeeze ngrok and change url in main() then in
app.run().

- To add members, you need to add gitlab user id in conf.py
"""
import requests

from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook

import conf
import ngrok
import response
import webhook


TEAMS_API = WebexTeamsAPI(access_token=conf.WEBEX_TEAMS_ACCESS_TOKEN)
app = Flask(__name__)


class User:
    """User_id is your gitlab id, you need to add it to MEMBERS dict.

    You can find your gitlab id on gitlab, settings.
    """
    def __init__(self, username, email=None):
        self.username = username
        self.github_username = conf.MEMBERS[self.username]
        self.email = email


class Github(User):
    def get_merge_requests(self):
        """Retrieve all opened merge requests with For Review label."""

        header = {'Authorization': f'token {conf.GITHUB_ACCESS_TOKEN}'}
        query = """
        {
          organization(login: "outscale") {
            id
            projects(first: 10) {
              edges {
                node {
                  id
                  name
                }
              }
            }
          }
        }
        """
        request = requests.get(
                url='https://api.github.com/graphql',
                json={'query': query},
                headers=header,
                verify=False
                )

        import pdb; pdb.set_trace()
        merge_requests = []
        for mr in res.json():
            merge_requests.append(
                    {
                        'assignee': mr['assignee']['name'],
                        'author': mr['author']['name'],
                        'delete_branch': mr['force_remove_source_branch'],
                        'id': mr['id'],
                        'labels': mr['labels'],
                        'squash': mr['squash'],
                        'title': mr['title'],
                        'url': mr['web_url'],
                        }
                    )

            self.merge_requests = merge_requests


def send_direct_message(email, message, markdown=None):
    if markdown:
        TEAMS_API.messages.create(toPersonEmail=email, markdown=message)
    else:
        TEAMS_API.messages.create(toPersonEmail=email, text=message)


def send_message_in_room(room_id, message):
    TEAMS_API.messages.create(roomId=room_id, text=message)


def create_user(email):
    """Create user with email from the person who send a message to the bot."""

    global user
    user = email.split("@")[0]
    user = Github(username=user, email=email)
    user.get_merge_requests()


@app.route('/webex', methods=['POST'])
def webex_events():
    """"Request event based on ngrok public url."""

    json_data = request.json
    webhook_obj = Webhook(json_data)

    message = TEAMS_API.messages.get(webhook_obj.data.id)
    bot = TEAMS_API.people.me()

    if message.personId == bot.id:
        # Message was sent by me (bot); do not respond.
        return 'OK'
    else:
        user_email = message.personEmail
        create_user(email=user_email)

        if message.text == '/all':
            data = response.merge_request(data=user.merge_requests)
            send_direct_message(email=user.email, message=data)

        if message.text == '/mr':
            data = response.details(data=user.merge_requests)
            send_direct_message(email=user.email, message=data)

        return 'OK'


@app.route('/github', methods=['POST'])
def github_events():
    """"Request event based on ngrok public url."""

    json_data = request.json
    print(json_data)

    return 'OK'


def main():
    """"Retrieve the public address from ngrok and create webhook."""

    ngrok_url = ngrok.get_ngrok_public_url()

    # Set the hook for webex
    webex_url = ngrok_url + '/webex'
    webhook.delete_webex(api=TEAMS_API)
    webhook.create_webex(api=TEAMS_API, url=webex_url)


if __name__ == '__main__':
    main()
    app.run(host='localhost', port=8080)
