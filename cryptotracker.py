import requests
import json

coinMap = {
    1:90,
    2:80,
    3:518,
    4:2710,
    5:58,
    6:33285,
    7:48543,
    8:2713,
    9:46971,
    10:2
    }

def choose_coin():
    while True:
        try:
            key = int(input("\nenter the number: "))
            if key in coinMap:
                return coinMap[key]
            else:
                print("please choose in the range")

        except:
            print("invalid number")

        




def fetch_price(coinID):
    url = (f"https://api.coinlore.net/api/ticker/?id={coinID}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException:
        print("API Request Failed")
        return None



def display_price(data):
    print("\nCoin: ", data[0]["symbol"])
    print("Price: $", data[0]["price_usd"])
    print("Change in 24hour: ", data[0]["percent_change_24h"],"%")
    print("Market cap: $", data[0]["market_cap_usd"])

def main():
    print(coins)
    coinID = choose_coin()
    data = fetch_price(coinID)
    if data:
        display_price(data)

    print(options_print)
    return coinID



print("=======CRYPTO TRACKER=======\n\nChoose number only\n")
coins = "1 BTC\n2 ETH\n3 USDT \n4 BNB\n5 XRP\n6 USDC\n7 SOL\n8 TRX\n9 STETH\n10 DOGE"
options_print = "\n1 Refresh Price \n2 Change Coin \n3 Exit"

def run_tracker(coinID):
        while True:
            try:
                option = int(input("Choose option: "))
                if option == 1:
                    data = fetch_price(coinID)
                    if data:
                        display_price(data)
                        print(options_print)

                elif option == 2:
                    coinID = main()
            
                elif option == 3:
                    return

                else:
                    print("invalid option.")

            
            except ValueError:
                print("Please enter valid number.")

run_tracker(main())
