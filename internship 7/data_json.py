import json

try:
    with open("ws.json","r") as file:
        ws_lst = json.load(file)
        for w in ws_lst:
            print(f"ID:{w['id']} Nane:{w['wname']} year:{w['year']}")
except Exception as e:
    print(str(e))
