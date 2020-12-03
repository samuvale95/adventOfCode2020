def read_input(filename):
    pass_policys=[]
    with open(filename, 'r') as f:
        for line in f:
            record = line.split(':')
            rng, value = [i.strip() for i in record[0].split(' ')]
            psw = record[1].strip()
            pass_policys.append({'range': rng, 'value': value, 'psw': psw})
    return pass_policys

def check_is_valid(d):
    _min, _max = [int(n) for n in d['range'].split('-')]
    value = d['value']
    psw = d['psw']
    occ = psw.count(value)
    if(_min<=occ<=_max): return True
    else: return False

def check_is_valid_modified(d):
    _min, _max = [int(n) for n in d['range'].split('-')]
    value = d['value'].strip()
    psw = d['psw'].strip()

    if((psw[_min-1]==value) and (psw[_max-1]!=value) or (psw[_max-1]==value) and (psw[_min-1]!=value)): return True
    else: return False

if __name__ == "__main__":
    passible_psw = read_input('in.txt')
    count=0
    for i in range(0, len(passible_psw)):
        if(check_is_valid_modified(passible_psw[i])):
            count+=1
    print(count)