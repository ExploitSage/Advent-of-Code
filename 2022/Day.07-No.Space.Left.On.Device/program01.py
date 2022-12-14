import sys

size_sum = 0

def dir_size(dir, name):
    global size_sum
    size = 0
    for e in dir:
        if type(dir[e]) == type(dict()):
            size += dir_size(dir[e],e)
        else:
            size += dir[e]
    
    if size < 100000:
        size_sum += size
    
    return size

fs = {}

cwd = None
cwd_path = None

for line in sys.stdin:
    command = line.strip().split()

    if command[0] == '$':
        if command[1] == 'cd':
            if cwd == None:
                fs[command[2]] = {}
                cwd = fs[command[2]]
                cwd_path = [command[2]]
            else:
                if command[2] == '..':
                    cwd_path.pop()
                    cwd = fs[cwd_path[0]]
                    for path in cwd_path[1:]:
                        cwd = cwd[path]
                else:
                    if command[2] not in cwd:
                        cwd[command[2]] = {}
                    cwd = cwd[command[2]]
                    cwd_path.append(command[2])
    else:
        if command[0] == 'dir':
            cwd[command[1]] = {}
        elif command[0].isnumeric():
            cwd[command[1]] = int(command[0])

dir_size(fs['/'],'/')

print(size_sum)
