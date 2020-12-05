def read_file(filename):
    with open(filename, 'r') as f:
        return [{'row':line.strip()[:7], 'col':line.strip()[7:]} for line in f]

def binary_search(line, rng):
    if(len(line) == 1):
        if(line == 'B' or line == 'R'): return rng[1]
        else: return rng[0]

    if(line[0]=='B' or line[0]=='R'):
        return binary_search(line[1:], (rng[0]+round((rng[1]-rng[0])/2),rng[1]))
    else:
        return binary_search(line[1:], (rng[0], rng[0]+int((rng[1]-rng[0])/2)))

if __name__ == "__main__":
    tickets = read_file('in.txt')
    all_id = [binary_search(i.get('row'),(0,127)) * 8 + binary_search(i.get('col'),(0,7)) for i in tickets]
    print(set(range(min(all_id), max(all_id))).difference(set(all_id)))