import json 
import boto3
from datetime import datetime

def lambda_handler(event, context):
    """Writes the data to a date-encoded S3 folder.

    The folder structure should make it easy to locate rates from a given date and time.

    Args:
        event: dictionary in the same format as the output from the transform function
        context: supplied by AWS

    Returns:
        dictionary, either {'result': 'Success'} if successful or {'result': 'Failure'} otherwise
    """
    # replace this code
    bucket_name = 'nc-de-currency-data-20250213150922346500000001'
    file_name = f'{datetime.now()}_eur_usd_exchange_rates.json'

    file_content = json.dumps(event) + "\n"

    s3 = boto3.client('s3')
    s3.put_object(Body=file_content, Bucket=bucket_name, Key=file_name)

    return {"result": "Houston, we have liftoff"}
