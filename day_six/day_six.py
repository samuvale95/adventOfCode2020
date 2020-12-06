def read_input(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n\n')

if __name__ == "__main__":
    answears = read_input('in.txt')
    print(sum([len(set.intersection(*i)) for i in [[set(list(i)) for i in line.split('\n')] for line in answears]]))