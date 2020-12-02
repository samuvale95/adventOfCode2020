def read_input(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers

if __name__ == "__main__":
    numbers = read_input('in.txt')

    for i in range(0, len(numbers)):
        for j in range(1, len(numbers)):
            for k in range (2, len(numbers)):
                if(numbers[i]+numbers[j]+numbers[k] == 2020):
                    print(numbers[i]*numbers[j]*numbers[k])

