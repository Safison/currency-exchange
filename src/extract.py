import requests


def lambda_handler(event, context):
    """Extracts the latest currency data from the API.

    In the first instance, the function only needs to extract the EUR/USD rate.

    Args:
        event: an empty dictionary
        context: context object provided by AWS

    Returns:
        dictionary e.g.
        {
                "date": "2024-07-30",
                "eur": {
                        "gbp": 0.84175906,
                        "jpy": 166.80563884,
                        "usd": 1.08167213,
            ...
                        }
        }
    """
    # replace this code
    print(requests.__version__)
    return {
        "date": "2024-07-30",
        "eur": {"gbp": 0.84175906, "jpy": 166.80563884, "usd": 1.08167213},
    }
