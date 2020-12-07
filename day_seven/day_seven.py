def read_input(filename):
    with open(filename, 'r') as f:
        return {line.split('bags contain')[0].strip(): [i.replace('.','').replace('bags', '').replace('bag','').strip()[2:] for i in line.split('bags contain')[1].split(',')] for line in f}

def read_input_2(filename):
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
        if('other' in n): continue
        elif('shiny gold' in node): return True
        else: res.append(navigate(n, tree))
    return any(res)

def deep_calc(node, tree):
    if(node=='no other'): return 0
    return sum([i[0] + (i[0]*deep_calc(i[1], tree)) for i in tree.get(node)])

def first_part():
    cnt=0
    tree = read_input('in.txt')
    for k,_ in tree.items():
        if k!='shiny gold' and navigate(k, tree) == True: cnt+=1
    print(cnt)

def second_part():
    pass

if __name__ == "__main__":

    print(deep_calc('shiny gold', read_input_2('in.txt')))

