def part_one():
        mask = ''.zfill(36)
        mem={}

        def apply_mask(value, mask):
            value=list(value)
            for i in range(0, len(mask)):
                if(mask[i]!='X'):
                    value[i]=mask[i]
            return ''.join(value)

        with open('in.txt', 'r') as f:
            for line in f:
                k, v = [i.strip() for i in line.split('=')]
                if(k=='mask'):
                    mask=v
                else:
                    mem[int(k[4:-1])] = apply_mask("{0:b}".format(int(v)).zfill(36), mask)

        tot=0
        for _, v in mem.items():
            tot+=int(v,2)
        print(tot)

def part_two():
    mask = ''.zfill(36)
    mem={}

    def make_combinations(value):
        queue = [value]
        result=[]
        while(len(queue)>0):
            element = list(queue.pop())
            for i in range(0, len(element)):
                if(element[i]=='X'):
                    for j in ['0','1']:
                        element[i]=j
                        if('X' in element): queue.append(''.join(element))
                        else: result.append(''.join(element))
                    break
        return result

    def apply_mask(value, mask):
        value=list(value)
        for i in range(0, len(mask)):
            if(mask[i]=='X'):
                value[i]='X'
            elif(mask[i] == '1'):
                value[i]='1'

        return make_combinations(''.join(value))

    with open('in.txt', 'r') as f:
        for line in f:
            k, v = [i.strip() for i in line.split('=')]
            if(k=='mask'):
                mask=v
            else:
                for i in apply_mask("{0:b}".format(int(k[4:-1])).zfill(36), mask):
                    mem[int(i,2)] = "{0:b}".format(int(v)).zfill(36)

    tot=0
    for _, v in mem.items():
        tot+=int(v,2)
    print(tot)

if __name__ == "__main__":
    part_one()
    part_two()