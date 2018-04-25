scores = [60,50,60,58,54,54,
        58,50,52,54,28,69,
        34,55,51,52,44,51,
        69,64,66,55,52,61,
        46,31,57,52,44,18,
        41,53,55,61,51,44]

hight_scrore = 0

length = len(scores)
for i,score in enumerate(scores):
    print('Bubble test:'+str(i),'score:'+str(score))
    if score > hight_scrore:
        hight_scrore = score
print('Bubbles tests:',length)
print('Highest bubble score:',hight_scrore)

best_solutions = []
for i,score in enumerate(scores):
    if hight_scrore == score:
        best_solutions.append(i)

print('Solutions with the hightest score:', best_solutions)