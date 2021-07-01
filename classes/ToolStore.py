from classes import Translate
import json
import urllib.request


def priceFormatter(price, tt=",.2f"):
    if Translate.lang == "nl":
        new_price = str(format(price, tt)).replace(".", "m").replace(",", ".").replace("m", ",")

    else:
        new_price = str(format(price, tt))
    return new_price


def priceFormatterIncludeCalc(price, tt=",.2f"):
    if Translate.lang == "nl":
        new_price = str(format(priceCalculator(price), tt)).replace(".", "m").replace(",", ".").replace("m", ",")

    else:
        new_price = str(format(priceCalculator(price), tt))
    return new_price


def priceCalculator(price):
    return price * currencies[Translate.countries[Translate.state][1]][1]


def moneySymbol():
    return currencies[Translate.countries[Translate.state][1]][0]

def getCurrency(curr):
    url = "https://free.currconv.com/api/v7/convert?q=USD_" + str(curr) + "&compact=ultra&apiKey=64ad247e97504cc264a5"
    return json.loads(urllib.request.urlopen(url).read())["USD_" + str(curr)]


currencies = {
    "EUR": ["€", getCurrency("EUR")],
    "GBP": ["£", getCurrency("GBP")],
    "USD": ["$", 1],
}

