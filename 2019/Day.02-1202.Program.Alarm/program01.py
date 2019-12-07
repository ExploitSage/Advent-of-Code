import sys

ADD=1
MUL=2
HALT=99
INSTRUCTION_LEN=4

prog_mem = [int(x.strip()) for x in sys.stdin.readline().strip().split(',')]
prog_mem[1]=12
prog_mem[2]=2
pos = 0

while prog_mem[pos] != HALT:
	opcode = prog_mem[pos]
	op1_addr = prog_mem[pos+1]
	op2_addr = prog_mem[pos+2]
	res_addr = prog_mem[pos+3]
	if opcode == ADD:
		prog_mem[res_addr] = prog_mem[op1_addr]+prog_mem[op2_addr]
	elif opcode == MUL:
		prog_mem[res_addr] = prog_mem[op1_addr]*prog_mem[op2_addr]
	pos += INSTRUCTION_LEN

print(prog_mem[0])