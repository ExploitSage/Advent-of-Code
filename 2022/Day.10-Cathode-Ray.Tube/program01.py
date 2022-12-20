import sys

tick = 0
register = 1
signal_sum = 0
double_action = False

for line in sys.stdin:
    command = [e for e in line.strip().split()]
    if command[0] == 'addx':
        double_action = True

    for i in range(2 if double_action else 1):        
        if tick+1 in range(20,220+1,40):
            signal_sum += (tick+1)*register
        
        if double_action and i == 1:
            register += int(command[1])
            double_action = False
        
        tick += 1

print(signal_sum)
