def read_input(filename):
    with open(filename, 'r') as f:
        depart_time = int(f.readline().strip())
        return depart_time, [int(i.strip()) for i in f.readline().split(',') if i.strip()!='x']

def part_one():
    dep_time, bus_lines = read_input('in.txt')
    max_len = dep_time+max(bus_lines)

    for k, v in {i: [bus for bus in bus_lines if i%bus == 0] for i in range(dep_time, max_len)}.items():
        if(len(v)!=0):
            print(v[0]*(k-dep_time))
            break

def part_two():
    def read_input(filename):
        with open(filename, 'r') as f:
            depart_time = int(f.readline().strip())
            return depart_time, [int(i.strip()) if i.strip()!='x' else i.strip() for i in f.readline().split(',')]

    def get_bus_line_set(index, bus_lines):
        res=[]
        for i in range(0, len(bus_lines)):
            if(bus_lines[i]=='x'):
                res.append(bus_lines[i])
            elif((index+i)%bus_lines[i]==0):
                res.append(bus_lines[i])
        return res

    _,bus_lines=read_input('in.txt')
    print(bus_lines)
    index=100000000000000
    while(True):
        if(index%bus_lines[0]==0):
            if(bus_lines == get_bus_line_set(index, bus_lines)):
                print(index)
                break
            else:
                index+=bus_lines[0]-1
        else: index+=bus_lines[0]-1
        index+=1

if __name__ == "__main__":
    part_one()
    part_two()