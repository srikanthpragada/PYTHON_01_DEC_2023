# Calculate discount and net price

#input
price = int(input("Enter price :"))

#process
if price > 10000:
    discount = price * 20 // 100
else:
    discount = price * 10 // 100

net_price = price - discount

#output
print(f'Price        {price:8}')
print(f'-Discount    {discount:8}')
print(f'Net Price    {net_price:8}')


