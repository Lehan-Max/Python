import csv
data_list = [
    {"id":10001, "wname":"python","year":"2001"},
    {"id":10002, 'wname':'UI','year':'2002'},
    {"id":10004, 'wname':'AI','year':'2003'}
]
try:
    with open("ws.csv","w",newline="") as file:
        heading = ['id','wname','year',]
        obj = csv.DictWriter(file,fieldnames = heading)
        obj.writeheader()
        obj.writerows(data_list)
except Exception as e:
    print(str(e))
