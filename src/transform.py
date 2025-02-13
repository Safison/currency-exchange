import pprint
def lambda_handler(event, context):
    """Transforms the data to give the required rates against USD.

    The output should include the reverse rate to 6 decimal places.

    Args:
        event: a dictionary in the form output by the extract function.
        context: supplied by AWS

    Returns:
        dictionary e.g. {
            "eur": {
                "rate": 1.08167213,
                "reverse_rate": 0.924495
            }
        }

    """
    # replace this code
    eur_usd_fwd_rate = event['eur']['usd']
    eur_usd_rev_rate = 1 / eur_usd_fwd_rate
    
    return {"eur": {"rate": eur_usd_fwd_rate, "reverse_rate": eur_usd_rev_rate}}
