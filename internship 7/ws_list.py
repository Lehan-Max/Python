data_list = [
    {"id":10001, "wname":"python","year":"2001"},
    {"id":10002, 'wname':'UI','year':'2002'},
    {"id":10004, 'wname':'AI','year':'2003'}

]
try:
    with open('ws.txt','w') as file:
        for data in data_list:
            line = f'{data["id"]},{data["wname"]},{data["year"]}\n'
            file.write(line)
except Exception as e:
    print(str(e))