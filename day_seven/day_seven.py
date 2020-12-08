def read_input(filename):
    with open(filename, 'r') as f:
        tree = {}
        for line in f:
            k, v = [i.strip() for i in line.split('bags contain')]
            v=[(int(i[0]),i[2:]) if i!='no other' else (0, i) for i in [i.strip() for i in v.replace('.',',').replace('bags','').replace('bag', '').split(',') if i != '']]
            tree[k]=v
        return tree

def navigate(node ,tree):
    res = []
    for n in tree.get(node):
        if('other' in n[1]): continue
        elif('shiny gold' in node): return True
        else: res.append(navigate(n[1], tree))
    return any(res)

def deep_calc(node, tree):
    if(node=='no other'): return 0
    return sum([i[0] + (i[0]*deep_calc(i[1], tree)) for i in tree.get(node)])

def first_part():
    cnt=0
    tree = read_input('in.txt')
    for k in tree.keys():
        if k!='shiny gold' and navigate(k, tree) == True: cnt+=1
    print(cnt)

def second_part():
    print(deep_calc('shiny gold', read_input('in.txt')))

if __name__ == "__main__":
    first_part()
    second_part()