import sys

rope = [[0,0] for know in range(10)]
tail_positions = []

for line in sys.stdin:
    direction, distance = [int(e) if e.isnumeric() else e for e in line.strip().split()]

    for move in range(distance):
        for knot in range(len(rope)):
            if knot == 0:
                # Move head
                if direction == 'U':
                    rope[knot][1] += 1
                if direction == 'D':
                    rope[knot][1] -= 1
                if direction == 'L':
                    rope[knot][0] -= 1
                if direction == 'R':
                    rope[knot][0] += 1
            else:
                # Move tails
                x_diff = rope[knot-1][0]-rope[knot][0]
                y_diff = rope[knot-1][1]-rope[knot][1]
                
                
                if abs(x_diff) > 1:
                    rope[knot][0] += 1 if x_diff > 0 else -1
                    if abs(y_diff) > 0:
                        rope[knot][1] += 1 if y_diff > 0 else -1
                elif abs(y_diff) > 1:
                    rope[knot][1] += 1 if y_diff > 0 else -1
                    if abs(x_diff) > 0:
                        rope[knot][0] += 1 if x_diff > 0 else -1
                
                if knot == len(rope)-1:
                    tail_positions.append(tuple(rope[knot]))


print(len(set(tail_positions)))
