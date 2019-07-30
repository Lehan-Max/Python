
try:
    with open("data.txt") as fin, open("data1.txt","w") as fout:
        lines = fin.readlines()
        lines = [l.upper() for l in lines]
        fout.writelines(lines)
    
        #for line in lines:
         #   upperr = line.upper()
          #  fout.write(upperr)

except Exception as e:
    print(f"File not found please check path {e}")