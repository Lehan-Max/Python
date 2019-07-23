names = ["PKM", "allen", "raj","Rani","Nvs","cs", "mcs","PKM"]
c_name={}
for name in names:
    if c_name.get(name)==None:   #compare: if key doesn't exist return none
        c_name[name] = 1
    else:
        c_name[name]+= 1
print(c_name) #prints how mant times name is present