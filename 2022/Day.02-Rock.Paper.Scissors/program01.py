import sys

score = 0

for line in sys.stdin:
    match = [ord(line.strip().split()[0])-65, ord(line.strip().split()[1])-88]
    score += match[1]+1
    score += ((match[1]-match[0]+1)%3)*3

print(score)
