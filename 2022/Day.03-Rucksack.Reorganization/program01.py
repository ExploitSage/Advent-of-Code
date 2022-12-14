import sys

priority = 0

for line in sys.stdin:
    rucksack = line.strip()
    rucksack_left = list(rucksack[0:len(rucksack)//2])
    rucksack_right = list(rucksack[len(rucksack)//2:])

    dups = set([item for item in rucksack_left if item in rucksack_right])
    for item in dups:
        if item.isupper():
            priority += ord(item)-64+26
        else:
            priority += ord(item)-96
    
print(priority)
