import sys

draw_scores = [('A',1),('B',2),('C',3)]
lose_scores = [('A',3),('B',1),('C',2)]
win_scores =  [('A',2),('B',3),('C',1)]

score = 0

for line in sys.stdin:
    match = tuple(line.strip().split())

    if match[1] == 'X':
        score+=list(filter(lambda x:match[0] in x, lose_scores))[0][1]
    if match[1] == 'Y':
        score+=list(filter(lambda x:match[0] in x, draw_scores))[0][1]+3
    if match[1] == 'Z':
        score+=list(filter(lambda x:match[0] in x, win_scores))[0][1]+6

print(score)