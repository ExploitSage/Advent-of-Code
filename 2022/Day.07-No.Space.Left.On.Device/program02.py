import sys

dir_sizes = {}

def dir_size(dir, name):
    global dir_sizes
    size = 0
    for e in dir:
        if type(dir[e]) == type(dict()):
            size += dir_size(dir[e],e)
        else:
            size += dir[e]
    
    dir_sizes[name] = size
    
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

required_size = 30000000-(70000000-dir_sizes['/'])

dir_sizes = sorted(dir_sizes.items(),key=lambda x:x[1])

for e in dir_sizes:
    if e[1] >= required_size:
        print(e[1])
        break
