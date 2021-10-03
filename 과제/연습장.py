def cal_upper(price):
        increment = price * 0.3
        upper_price = price + increment
        return upper_price

b = cal_upper(10000)
print(b)