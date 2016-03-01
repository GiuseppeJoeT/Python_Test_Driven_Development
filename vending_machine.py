# we define pur list of coins in pence
lCoins = [100, 50, 20, 10, 5, 2, 1]


def give_change(nAmount):
    lChange = []
    # We define an empty list which will hold our list of coins

    for nCoin in lCoins:
        if nCoin <= nAmount:
            nAmount -= nCoin
            lChange.append(nCoin)
    return lChange