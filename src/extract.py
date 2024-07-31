import requests

def lambda_handler(event, context):
    print(requests.__version__)
    return {
	"date": "2024-07-30",
	"eur": {
		"gbp": 0.84175906,
		"jpy": 166.80563884,
		"usd": 1.08167213
        }
    }