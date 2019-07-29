data_list = [
            [1001,'python',2016,1,'mite'],
            [1002,'web',2015,2,'mit'],
            [1001,'python Language',2017,3,'mite']
]

try:
    with open('ws.txt','w') as file:
        for data in data_list:
            line = f'{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n'
            file.write(line)
except Exception as e:
    print(str(e))