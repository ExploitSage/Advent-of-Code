import sys

total_fuel = 0

for line in sys.stdin:
	mass = int(line.strip())
	while max(0,mass) > 6:
		fuel = mass//3-2
		total_fuel+=fuel
		mass = fuel

print total_fuel
