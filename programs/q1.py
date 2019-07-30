try:
    with open("u_story.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(" ")
            for word in words:
                word = word.strip().strip("\n").replace(',','').replace(',','')
            print(word)
                
                

    
except:
    print(" ")