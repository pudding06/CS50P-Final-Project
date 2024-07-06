import requests
from currency_converter import is_valid_currency, get_conversion_rate

key = "fca_live_LiEDC9ZCueaLNrSkLJgqVeitOfM2EQYizV5XoZPx"

def test_is_valid_currency_True():
    assert is_valid_currency("USD") == True
    assert is_valid_currency("SGD") == True

def test_is_valid_currency_False():
    assert is_valid_currency("foo") == False
    assert is_valid_currency("bar") == False

def test_freecurrenciesapi_currencies():
    url = f"https://api.freecurrencyapi.com/v1/currencies?apikey={key}"
    response = requests.get(url)
    assert response.status_code == 200

def test_freecurrenciesapi_latest():
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={key}"
    response = requests.get(url)
    assert response.status_code == 200
