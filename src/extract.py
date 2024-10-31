import requests

API_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/{apiVersion}/{endpoint}"

def get_exchange_rate(date, cur_from, cur_to):
    """Gets currency data from the Free Currency Exchange Rates API.
    Args:
        date (datetime): the date to get the rate for
        cur_from (str): currency code to exchange from
        cur_to (str): currency code to exchange to

    Returns:
        rate (float): the exchange rate for 
    """
    url = "{API_URL}@{date}/{apiVersion}/{endpoint}"
    pass

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
