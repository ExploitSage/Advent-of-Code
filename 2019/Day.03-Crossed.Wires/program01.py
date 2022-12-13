import sys

lines = []
intersections = set()
least_dist = None

for line in sys.stdin:
	segments = [(segment[0],int(segment[1:])) for segment in line.strip().split(',')]
	line = []
	current_point=(0,0) # Central Port
	
	for segment in segments:
		for point in range(segment[1]):
			if segment[0] == "U":
				current_point=(current_point[0],current_point[1]+1)
			elif segment[0] == "R":
				current_point=(current_point[0]+1,current_point[1])
			elif segment[0] == "D":
				current_point=(current_point[0],current_point[1]-1)
			elif segment[0] == "L":
				current_point=(current_point[0]-1,current_point[1])
			line.append((current_point[0],current_point[1]))

	lines.append(line)

print(min([abs(x)+abs(y) for (x, y) in list(set(lines[0]) & set(lines[1]))]))