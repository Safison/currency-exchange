import requests
import pprint



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
    URL = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2025-02-13/v1/currencies/eur.json'
    curr_rate = requests.get(url=URL)
    dict_curr_rate = curr_rate.json()
    #return dict_curr_rate
    # print(requests.__version__)
    
    curr_date = dict_curr_rate['date']
    float_eur_usd = dict_curr_rate['eur']['usd']
    return {
        "date": curr_date,
        "eur": {"usd": float_eur_usd}
    }
