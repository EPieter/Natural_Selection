from classes import Translate


def priceFormatter(price):
    if Translate.lang == "nl":
        new_price = str(format(price, ",.2f")).replace(".", "m").replace(",", ".").replace("m", ",")

    else:
        new_price = str(format(price, ",.2f"))
    return new_price


def moneySymbol():
    if Translate.lang == "nl":
        return "€"
    else:
        return "$"
