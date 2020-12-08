def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(lambda a: [a[0], int(a[1]), False],[line.split(' ')for line in f]))

def run_bootloader(prog):
    pc=0
    accumulator=0

    while(pc<len(prog)):
        if(prog[pc][2] == True): return -1

        prog[pc][2]=True
        if(prog[pc][0] == 'acc'):
            accumulator+=prog[pc][1]
            pc+=1
        elif(prog[pc][0] == 'jmp'):
            pc+=prog[pc][1]
        else: pc+=1

    return accumulator


if __name__ == "__main__":
    bootloader = read_input('in.txt')
    res=[]
    for i in range(0, len(bootloader)):
        bl=[i[:] for i in bootloader]
        if(bl[i][0]=='jmp'): bl[i][0]='nop'
        elif(bl[i][0]=='nop'): bl[i][0]=='jmp'
        else: continue

        res.append(run_bootloader(bl))
    print([i for i in res if i != -1])