# There is a shop with old-style cash registers.
# Rather than scanning items and pulling the price from a database, the price of each item is typed in manually. This method sometimes leads to errors. Given a list of items and their correct prices, compare the prices to those entered when each item was sold. Determine the number of errors in selling prices.


def priceCheck(products, productPrices, productSold, soldPrice):
    count = 0
    for i in range(len(productSold)):
        if productPrices[products.index(productSold[i])] != soldPrice[i]:
            count += 1
    return count



# contains weather details of various cities. Given a city name, get the current temperature of the city.
# To access the weather information, perform an HTTP GET request to:
# https://jsonmock.hackerrank.com/api/weather?name=<name>
# where ‹name> is the city name to query. The name not case-sensitive.
# For example, a have at lease one weather record in the response.


def getTemperature(name):
    import requests
    response = requests.get(f"https://jsonmock.hackerrank.com/api/weather?name={name}")
    data = response.json()
    return int(data['data'][0]['weather'].split()[0])


