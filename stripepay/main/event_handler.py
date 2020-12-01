from djstripe import webhooks


@webhooks.handler("customer.created")
def my_handler(event, **kwargs):
    print("==========================", event)
    print("--------------------------", **kwargs)
