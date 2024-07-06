import tabulate

from freecurrencyapi import Client

# Authentication key for getfreecurrencies API
key = "fca_live_LiEDC9ZCueaLNrSkLJgqVeitOfM2EQYizV5XoZPx"

# Creating a client object and use the .currencies() method to request the availible currencies supported by the API
client = Client(key)
data = client.currencies()
currencies = list(data["data"].keys())
names = []
for currency in currencies:
    c = dict()
    c["Currencies supported"] = data["data"][currency]["name"]
    c["Symbol"] = currency
    names.append(c)

# Print a table of supported currencies for the user
table = tabulate.tabulate(names, headers="keys", tablefmt="rounded_grid")
print(table)

def main():
    # Get user data
    old_currency = get_currency("Currency (symbol) you currently have: ")
    money = get_money("Amount: ")
    new_currency = get_currency("Currency (symbol) to exchange to: ")
    conversion_rate = get_conversion_rate(old_currency, new_currency)
    new_money = round((money * conversion_rate), 2)
    money = f"{money:.2f}"

    # Print information to user
    print(f"You have decided to exchange ${money} {old_currency} into {new_currency}")
    print(f'That is a conversion of {data["data"][old_currency]["name_plural"]} to {data["data"][new_currency]["name_plural"]}')
    print(f"The exchage rate is currently about {conversion_rate:.2f}")
    print(f'{data["data"][old_currency]["symbol"]}{money} is converted to {data["data"][new_currency]["symbol"]}{new_money}')
    
def get_currency(prompt):
    while True:
        try:
            currency = input(prompt).strip().upper()
        except:
            print("Invalid Currency")
        if is_valid_currency(currency):
            return currency
        else:
            print("Invalid Currency")


def is_valid_currency(currency):
    # Check if the currency user has entered is valid
    if currency in currencies:
        return True
    else:
        return False

def get_money(prompt):
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            print("Invalid amount")

def get_conversion_rate(old, new):
    result = client.latest(currencies=[old, new])
    rate = result["data"][new] / result["data"][old]
    return rate



if __name__ == "__main__":
    main()
