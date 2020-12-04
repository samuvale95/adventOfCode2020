def read_input(filename):
    with open(filename, 'r') as f:
        all_input = [[j.split(':') for j in i.split(' ')] for i in [p.replace('\n', ' ') for p in f.read().split('\n\n')]]
        return [dict(i) for i in all_input]

def is_passport(p):
    return (len(p) == 8) or (len(p) == 7 and p.get('cid') is None)

def data_is_valid(p):
    funcs = [
        lambda p: 1920<=int(p['byr'])<=2002,
        lambda p: 2010<=int(p['iyr'])<=2020,
        lambda p: 2020<=int(p['eyr'])<=2030,
        lambda p: (150<=int(p['hgt'][:-2])<=193 if p['hgt'][-2:] == 'cm' else 59<=int(p['hgt'][:-2])<=76) if 'cm' in p['hgt'] or 'in' in p['hgt'] else False,
        lambda p: p['hcl'][0]=='#' and all([0<=int(i)<=9 if i.isdigit() else 'a'<=i<='f' for i in list(p['hcl'])[1:]]),
        lambda p: len(p['ecl'])==3 and p['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'],
        lambda p: p['pid'].isdigit() and len(p['pid'])==9,
    ]
    return all(list(map(lambda f: f(p), funcs)))

if __name__ == "__main__":
    passports = read_input('in.txt')
    count=0

    for p in passports:
        if(is_passport(p) and data_is_valid(p)): count+=1

    print(count)