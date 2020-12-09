from itertools import combinations

def read_input(filename):
    with open(filename, 'r') as f:
        return [int(i.strip()) for i in f]

def find_number(padding, cipher):
    list_comb = [sum(j) for j in combinations([cipher[i] for i in range(0, padding)], 2)]

    for index in range(padding, len(cipher)):
        if(cipher[index] not in list_comb): return cipher[index]
        list_comb = [sum(j) for j in combinations([cipher[i] for i in range(index+1-padding, index+1)], 2)]

def find_encryption_weakness(number, cipher):
    count_index=0
    for _ in cipher:
        index=count_index
        cont_set=[]
        while(number-sum(cont_set)>=0):
            if(number-sum(cont_set)==0):
                return min(cont_set)+max(cont_set)
            else:
                cont_set.append(cipher[index])
                index+=1
        count_index+=1

if __name__ == "__main__":
    cipher = read_input('in.txt')

    number = find_number(25, cipher)
    print(find_encryption_weakness(number, cipher))