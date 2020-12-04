def read_input(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]

if __name__ == "__main__":
    numbers = read_input('in.txt')
    for i in range(0, len(numbers)):
        for j in range(1, len(numbers)):
            for k in range (2, len(numbers)):
                if(numbers[i]+numbers[j]+numbers[k] == 2020):
                    print(numbers[i]*numbers[j]*numbers[k])