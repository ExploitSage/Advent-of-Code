import sys

packet_size = 14
buffer = []

for line in sys.stdin:
    for i in range(len(line.strip())):
        buffer.append(line[i])
        while len(buffer) > packet_size:
            buffer.pop(0)
        if len(set(buffer)) == packet_size:
            print(i+1)
            break
