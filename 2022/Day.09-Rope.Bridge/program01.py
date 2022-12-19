import sys

head = [0,0]
tail = [0,0]
tail_positions = []

for line in sys.stdin:
    direction, distance = [int(e) if e.isnumeric() else e for e in line.strip().split()]

    for move in range(distance):

        # Move head
        if direction == 'U':
            head[1] += 1
        if direction == 'D':
            head[1] -= 1
        if direction == 'L':
            head[0] -= 1
        if direction == 'R':
            head[0] += 1

        # Move tail
        x_diff = head[0]-tail[0]
        y_diff = head[1]-tail[1]
        
        
        if abs(x_diff) > 1:
            tail[0] += 1 if x_diff > 0 else -1
            if abs(y_diff) > 0:
                tail[1] += 1 if y_diff > 0 else -1
        elif abs(y_diff) > 1:
            tail[1] += 1 if y_diff > 0 else -1
            if abs(x_diff) > 0:
                tail[0] += 1 if x_diff > 0 else -1
        
        tail_positions.append(tuple(tail))


print(len(set(tail_positions)))
