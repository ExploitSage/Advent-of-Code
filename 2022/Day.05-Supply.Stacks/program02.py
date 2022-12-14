import sys

stacks = None

for line in sys.stdin:
    # Stack Parsing
    if '[' in line:
        if stacks == None:
            stacks = [[] for e in range(len(line)//4)]
        
        for idx in range(len(line)):
            if line.startswith('[', idx):
                stacks[idx//4].insert(0, line[idx+1])
    
    # Move Parsing
    elif 'move' in line:
        order = [int(val) for val in line.strip().split() if val.isnumeric()]
        stacks[order[2]-1].extend(stacks[order[1]-1][-1*order[0]:])
        del stacks[order[1]-1][-1*order[0]:]

print(''.join([stack[-1] for stack in stacks]))
