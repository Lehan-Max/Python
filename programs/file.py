try:

    fp = open("data.txt")
    data = "Line one \r\n"
    
    fp.write(data)
except Exception as e:
    print(f"{e}")
finally:
    fp.close()
