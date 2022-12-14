import sys

group = []
priority = 0

for line in sys.stdin:
    group.append(line.strip())
    if len(group) == 3:
        dups = set([item for item in group[0] if item in group[1] and item in group[2]])
        print(dups)
        for item in dups:
            if item.isupper():
                priority += ord(item)-64+26
            else:
                priority += ord(item)-96
        group = []
    
print(priority)
