#take individual score from the given list of score and total it and print

scores = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
        ]
res=0
for score in scores:  #takes individual list 'score' from 'scores'
    for s in score: #takes individual ele from 'score' and use to compute result
        res += s
print(f"sum: {res}")