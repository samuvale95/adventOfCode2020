from functools import reduce

def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

if __name__ == "__main__":
    mountain = read_input('in.txt')
    len_row = len(mountain[0])

    all_trees=[]
    slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]

    for i in slopes:
        x,y=i
        trees=0
        for _ in range(0, len(mountain)-1):
            if(y>len(mountain)): break
            if(mountain[y][x]=='#'): trees+=1
            x=(x+i[0])%len_row
            y+=i[1]
        all_trees.append(trees)

print(reduce(lambda a,b: a*b, all_trees))