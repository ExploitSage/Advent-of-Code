import sys

total_fuel = 0

for line in sys.stdin:
	mass = int(line.strip())
	total_fuel+=mass//3-2
	
print total_fuel
