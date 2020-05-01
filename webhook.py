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
