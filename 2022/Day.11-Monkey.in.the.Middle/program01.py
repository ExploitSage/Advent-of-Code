import sys
from functools import reduce

monkeys = []

for line in sys.stdin:
    if 'Monkey' in line:
        monkeys.append({})
        monkeys[-1]['inspected'] = 0
    elif 'Starting items' in line:
        monkeys[-1]['items'] = [int(e) for e in line.strip().replace(',','').split(':')[1].split()]
    elif 'Operation' in line:
        monkeys[-1]['operation'] = line.strip().split(':')[1].strip().split('=')[1].strip()
    elif 'Test' in line:
        monkeys[-1]['test'] = int(line.strip().split()[-1])
    elif 'If true' in line:
        monkeys[-1]['true'] = int(line.strip().split()[-1])
    elif 'If false' in line:
        monkeys[-1]['false'] = int(line.strip().split()[-1])

for round in range(20):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            # Inspect
            item = monkey['items'].pop(0)
            monkey['inspected'] += 1
            
            # Worry
            operation = lambda old: eval(monkey['operation'])
            item = operation(item)
            
            # Relief
            item = item//3
            
            # Test
            test = lambda x: x%monkey['test']==0

            if test(item):
                monkeys[monkey['true']]['items'].append(item)
            else:
                monkeys[monkey['false']]['items'].append(item)

print(reduce(lambda x,y:x*y,sorted([monkey['inspected'] for monkey in monkeys])[-2:]))
