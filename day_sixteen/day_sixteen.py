from itertools import permutations

def read_input(filename):
    with open(filename, 'r') as f:
        text_input=f.read().split('\n\n')
        class_def={}
        for line in text_input[0].split('\n'):
            k,v=[i.strip() for i in line.split(':')]
            v=[i.strip() for i in v.split('or')]
            class_def[k]=[[int(j) for j in i.split('-')] for i in v]

        my_ticket={}
        for i in text_input[1].split('\n')[1:]:
            pass

        other_tickets=[]
        for i in text_input[2].split('\n')[1:]:
            other_tickets.append([int(j.strip()) for j in i.split(',')])

        return class_def, my_ticket, other_tickets

def get_valid_tickets(other_tickets, class_def):
    valid_tickets=[]
    tot=0
    invalid=False
    for ticket in other_tickets:
        for number in ticket:
            if(all([(v[0][0]>number or number>v[0][1]) and (v[1][0]>number or number>v[1][1]) for _,v  in class_def.items()])):
                tot+=number
                invalid=True

        if not invalid: valid_tickets.append(ticket)
        invalid=False

    return tot, valid_tickets

def is_solution(field, valid_tickets, class_def):
    solution=[]
    for k in range(0, 3):
        for j in range(0, len(valid_tickets)):
            if((class_def[field[k]][0][0]<=valid_tickets[j][k]<=class_def[field[k]][0][1]) or (class_def[field[k]][1][0]<=valid_tickets[j][k]<=class_def[field[k]][1][1])):
                solution.append(True)
            else: solution.append(False)
        if(not all(solution)): return False, k
        solution=[]
    return True, None

if __name__ == "__main__":
    class_def, _, other_tickets = read_input('in.txt')

    first_part, valid_tickets=get_valid_tickets(other_tickets, class_def)

    print(first_part)

    #Find another way to not use a permutations

    # tickets_field = [field for field in class_def.keys()]

    # perm = permutations(tickets_field, len(tickets_field))
    # for i in perm:
    #     solution, index = is_solution(i, valid_tickets, class_def)
    #     if(solution):
    #         print(i)
    #         break
