retailItems = ["tomato" , "bread", "salt"]
retailPrices = [15.99, 4.99, 5.99]

onlineItems = ["tomato" , "bread", "salt", "water"]
onlinePrices = [15.89, 4.99, 6, 1.99]



def pricesDiff(retailItems, onlineItems, retailPrices, onlinePrices):
    counter = 0
    retail = dict(zip(retailItems,retailPrices))
    online = dict(zip(onlineItems,onlinePrices))
    for i in retail:
        if retail[i] != online[i]:
            counter += 1
    return counter


pricesDiff(retailItems, onlineItems, retailPrices, onlinePrices)