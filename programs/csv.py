import csv
class stock:
    def __init__(self, name, symbol, exchange, price):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.symbol}, {self.exchange}, {self.price}"
    
try:
    with open("stock_price.csv") as f:
        data  = csv.Dictreader(f, delimeter=",")
        stock_lst = []
        line = 0
    for d in data:
        if line == 0:
            line += 1
            continue
        stock_lst.append(Stock(*d))
    for s in stock_lst:
        if "K"in s.price:
            s.price = float(s.price.strip().replace("K",""))*1
            


    

    