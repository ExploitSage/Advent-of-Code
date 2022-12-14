import sys

overlaps = 0

for line in sys.stdin:
    pair = [tuple([int(e) for e in range.split('-')]) for range in line.strip().split(',')]
    if pair[0][0] <= pair[1][0] <= pair[0][1] or pair[0][0] <= pair[1][1] <= pair[0][1]:
        overlaps += 1
    elif pair[1][0] <= pair[0][0] <= pair[1][1] or pair[1][0] <= pair[0][1] <= pair[1][1]:
        overlaps += 1

print(overlaps)
