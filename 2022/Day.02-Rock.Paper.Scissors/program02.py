import sys

score = 0

for line in sys.stdin:
    match = [ord(line.strip().split()[0])-65, ord(line.strip().split()[1])-88]
    score += match[1]*3
    score += (((match[1]+match[0])+2)%3)+1

print(score)
