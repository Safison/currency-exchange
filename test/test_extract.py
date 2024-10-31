from src.extract import lambda_handler as extract_lambda_handler
from src.extract import get_currency_data

class TestGetCurrencyData:
    pass

class TestExtractLambdaHandler:
    def test_returned_data_format_is_as_expected():
        event = {}
        context = {}
        result = extract_lambda_handler(event, context)
        assert isinstance(result, dict)
        keys = ["date", "eur"]
        assert all([key in result.keys() for key in keys])
        assert len(result) == len(keys)
