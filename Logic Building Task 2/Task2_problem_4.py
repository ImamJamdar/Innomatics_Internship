# Problem 4: Count products above a price threshold

# list of prices
prices = [999,2300,2999,499,4033,100,300,4043]

count_above_1000 = 0

for price in prices:
    if price > 1000:
        count_above_1000 += 1

print("Total products above 1000:", count_above_1000)