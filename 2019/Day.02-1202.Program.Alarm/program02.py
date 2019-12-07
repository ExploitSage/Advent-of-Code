import sys

ADD=1
MUL=2
HALT=99
INSTRUCTION_LEN=4

prog_mem_orig = [int(x.strip()) for x in sys.stdin.readline().strip().split(',')]

for noun in range(0,100):
	for verb in range(0,100):
		prog_mem = prog_mem_orig[:]
		pos = 0
		prog_mem[1] = noun
		prog_mem[2] = verb

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
		
		if prog_mem[0] == 19690720:
			print("%s%s"%(noun,verb))
