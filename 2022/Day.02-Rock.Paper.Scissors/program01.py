import sys

choice_score = [('X',1),('Y',2),('Z',3)]

win_conditions = [('A','Y'),('B','Z'),('C','X')]
draw_conditions = [('A','X'),('B','Y'),('C','Z')]
lose_conditions = [('A','Z'),('B','X'),('C','Y')]

score = 0

for line in sys.stdin:
    match = tuple(line.strip().split())
    score+=(list(filter(lambda x:match[1] in x, choice_score))[0][1])
    if match in win_conditions:
        score+=6
    elif match in draw_conditions:
        score+=3
    elif match in lose_conditions:
        score+=0

print(score)