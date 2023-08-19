def discount(rate, price):
    discount_rate = int(price * rate / 100)
    new_price = price - discount_rate
    print("discount rate:", discount_rate)
    print("new price", new_price)


rate = int(input("rate:"))
price = int(input("price:"))
discount(rate, price)
