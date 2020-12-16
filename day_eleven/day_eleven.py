def read_input(filename):
    with open(filename, 'r') as f:
        l = [['.']+[i for i in line.strip()]+['.'] for line in f]
        fix = [ '.' for _ in range(0,len(l[0]))]
        l.insert(0, fix)
        l.append(fix)
        return l

def is_equal(map1, map2):
    for y in range(0, len(map1)):
        for x in range(0, len(map1[0])):
            if(map1[y][x]!=map2[y][x]): return False
    return True

def print_map(seats_map):
    for y in range(1, len(seats_map)-1):
        print(''.join(seats_map[y][1:-1]))

def get_seat_status_revisited(seats_map, x, y):
    res=[]

    n=y-1
    while(n>0):
        if(seats_map[n][x]=='L'): break
        if(seats_map[n][x]=='#'):
            res.append(seats_map[n][x])
            break
        n-=1

    n=y+1
    while(n<len(seats_map)):
        if(seats_map[n][x]=='L'): break
        if(seats_map[n][x]=='#'):
            res.append(seats_map[n][x])
            break
        n+=1

    j=x-1
    while(j>0):
        if(seats_map[y][j]=='L'): break
        if(seats_map[y][j]=='#'):
            res.append(seats_map[y][j])
            break
        j-=1

    j=x+1
    while(j<len(seats_map[0])):
        if(seats_map[y][j]=='L'): break
        if(seats_map[y][j]=='#'):
            res.append(seats_map[y][j])
            break
        j+=1

    n=y-1
    j=x-1
    while(j>0 and n>0):
        if(seats_map[n][j]=='L'): break
        if(seats_map[n][j]=='#'):
            res.append(seats_map[n][j])
            break
        n-=1
        j-=1

    n=y+1
    j=x+1
    while(n<len(seats_map) and j<len(seats_map[0])):
        if(seats_map[n][j]=='L'): break
        if(seats_map[n][j]=='#'):
            res.append(seats_map[n][j])
            break
        n+=1
        j+=1

    n=y+1
    j=x-1
    while(n<len(seats_map) and j>0):
        if(seats_map[n][j]=='L'): break
        if(seats_map[n][j]=='#'):
            res.append(seats_map[n][j])
            break
        n+=1
        j-=1

    n=y-1
    j=x+1
    while(n>0 and j<len(seats_map[0])):
        if(seats_map[n][j]=='L'): break
        if(seats_map[n][j]=='#'):
            res.append(seats_map[n][j])
            break
        n-=1
        j+=1

    return res

def change_status_revisited(seat_status, new_map, x, y):
    if(8-len(seat_status)==8):new_map[y][x] = '#'
    elif(len(seat_status)>=5):new_map[y][x] = 'L'

def get_seat_status(seats_map, x, y):
    return [seats_map[y+j][x+i] for j in [-1,0,1] for i in [-1,0,1] if j!=0 or i!=0]
def change_status(seat_status, new_map, x, y):
    if(len([i for i in seat_status if i in ['.', 'L']])==8):new_map[y][x] = '#'
    elif(len([i for i in seat_status if i == '#'])>=4):new_map[y][x] = 'L'

def count_occupied_seats(seats_map):
    return len([seats_map[y][x] for y in range(0, len(seats_map)) for x in range(0, len(seats_map[0])) if seats_map[y][x] == '#'])

if __name__ == "__main__":
    seats_map = read_input('in.txt')
    new_map=[line[:] for line in seats_map]

    continue_change=True
    while(continue_change):
        for y in range(1, len(seats_map)-1):
            for x in range(1, len(seats_map[0])-1):
                if(seats_map[y][x]!='.'):
                    change_status_revisited(get_seat_status_revisited(seats_map, x, y), new_map, x, y)
        if(is_equal(seats_map, new_map)):
            print(count_occupied_seats(new_map))
            continue_change=False
        seats_map=[line[:] for line in new_map]