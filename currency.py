# you will need to install requests if you somehow never have and ur gonna need an api key
# I think the part where you need to put the api key is decently obvious (hint: line 7)
import requests

def convert_currency(base_currency, target_currency, amount):
    #put api key in the place that tells you to put it
    url = f"https://v6.exchangerate-api.com/v6/PUT YOUR API KEY HERE!!!!!!!!!!!!/latest/{base_currency}" 
    response = requests.get(url)
    data = response.json()

    if data['result'] == 'success':
        conversion_rate = data['conversion_rates'].get(target_currency)
        if conversion_rate:
            return amount * conversion_rate
        else:
            raise Exception(f"Target currency {target_currency} not found.")
    else:
        raise Exception(f"Error: {data.get('error-type', 'Unknown error')}")

def CC():
        c1 = input("Type the form of currency you have (E.g. USD): ").upper()
        c2 = input("Type the form of currency you want to convert it to (E.g. EUR): ").upper()
        
        try:
            amount = float(input("Enter the amount: "))
            result = convert_currency(c1, c2, amount)
            print(f"{amount}{c1} = {result:.2f}{c2}")
        except Exception as e:
            print("Something went wrong: ", e)