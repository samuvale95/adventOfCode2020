from collections import defaultdict, deque
def read_input(filename):
    with open(filename, 'r') as f:
        return [int(i) for i in f.read().strip().split(',')]

if __name__ == "__main__":
    input_numbers = read_input('in.txt')
    input_numbers.insert(0,-1)
    mem = defaultdict(deque)

    for i in range(1, len(input_numbers)):
        mem[input_numbers[i]].append(i)

    last_number = input_numbers[-1]

    for i in range(len(input_numbers), 30000001):
        if(len(mem[last_number])==1):
            last_number=0
            mem[last_number].append(i)
        else:
            turns = mem[last_number]
            last_number=abs(turns[-1]-turns[-2])

            if(len(mem[last_number])==1):
                mem[last_number].append(i)
            else:
                mem[last_number].append(i)
    print(last_number)