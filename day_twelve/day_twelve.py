def read_input(filename):
    with open(filename, 'r') as f:
        return [(line[0], int(line[1:])) for line in f]

location = {'N':0, 'S':0, 'E':0, 'W':0, 'deg':90}

def forward(location, cmd):
    directions = {0:'N', 90:'E', 180:'S', 270:'W'}
    curr_dir = directions[location['deg']]
    location[curr_dir] += cmd[1]

def change_direction(location, cmd):
    if(cmd[0]=='R'):
        location['deg']=(cmd[1] + location['deg'])%360
    else:
        location['deg']=(location['deg'] - cmd[1])%360

def add_direction(location, cmd):
    location[cmd[0]] += cmd[1]

for cmd in read_input('in.txt'):
    if(cmd[0] in ['L','R']): change_direction(location, cmd)
    elif(cmd[0] == 'F'): forward(location, cmd)
    else: add_direction(location, cmd)

print(abs(location['N']-location['S'])+abs(location['E']-location['W']))