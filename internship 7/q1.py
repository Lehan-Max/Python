import json

try:
    with open("ws.json","r") as w, open("student.json","w") as s:
        s_lst = json.load(s)
        w_lst = json.load(w)

    for s in s_lst:
        for w in w_lst:
            if s["cid"] == w["id"]:
                print(f"{w['id']} {w['named']} {w['wname']} {w['year']}")
                break

except Exception as e:
    print(str(e)) 