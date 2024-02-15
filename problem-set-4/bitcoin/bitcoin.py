import requests
import sys

try:
    coin_count = float(sys.argv[1])
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    rate = float(r["bpi"]["USD"]["rate"].replace(',', ''))
    print(f"${(coin_count * rate):,.4f}")
except requests.RequestException:
    sys.exit()
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
