import conf


def create_webex(api, url):
    """Create a Webex Teams webhook pointing to flask URL."""
    print('Creating Webex Webhook...')
    webhook = api.webhooks.create(
        name='gitoune_webhook',
        targetUrl=url,
        resource='all',
        event='all',
    )
    print(webhook)
    print('Webex hook successfully created.')


def delete_webex(api):
    """Find a webhook by name."""
    for webhook in api.webhooks.list():
        if webhook.name == 'gitoune_webhook':
            print('Deleting Webex hook:', webhook.name, webhook.targetUrl)
            api.webhooks.delete(webhook.id)


def create_gitlab(api, url):
    """Create a Gitlab webhook pointing to flask URL."""

    # Curl --header "Private-Token: valid_token" https://gitlab.outscale.internal/api/v4/projects/218/hooks
    project = api.projects.get(conf.GITLAB_PROJECT_ID)

    print('Creating Gitlab Webhook...')
    # Push events: When true, the hook will fire on push events.
    webhook = project.hooks.create({'url': url, 'push_events': 1})
    print(webhook)
    print('Gitlab hook successfully created.')


def delete_gitlab(api):
    project = api.projects.get(conf.GITLAB_PROJECT_ID)

    for webhook in project.hooks.list():
        print('delete: ', webhook)
