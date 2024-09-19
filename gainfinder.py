def find_best_days(prices):
    minprice = float('inf')
    maxprofit = 0
    buyday = -1
    sellday = -1
    minday = 0

    for currentday in range(len(prices)):
        price = prices[currentday]

        if price < minprice:
            minprice = price
            minday = currentday

        currentprofit = price - minprice
        if currentprofit > maxprofit:
            maxprofit = currentprofit
            buyday = minday
            sellday = currentday

    return buyday + 1, sellday + 1, maxprofit


prices = [6, 2, 4, 7, 1]
buyday, sellday, maxprofit = find_best_days(prices)
print(f"{buyday}. gün alıp {sellday}. gün satmalısınız")
print(f"gain: {maxprofit}")
