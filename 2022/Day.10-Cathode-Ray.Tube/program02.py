import sys

tick = 0
register = 1
double_action = False
screen = []

for line in sys.stdin:
    command = [e for e in line.strip().split()]
    if command[0] == 'addx':
        double_action = True

    for i in range(2 if double_action else 1):        
        
        if register-1 <= tick%40 <= register+1:
            screen.append('#')
        else:
            screen.append('.')

        if double_action and i == 1:
            register += int(command[1])
            double_action = False
        
        tick += 1

for i in range(0,240,40):
    print(''.join(screen[i:i+40]))
