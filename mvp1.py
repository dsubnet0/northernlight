with open('a.txt', 'r') as file_a:
    lines_a = file_a.readlines()

with open('b.txt', 'r') as file_b:
    lines_b = file_b.readlines()

with open('a_not_b.txt', 'w') as a_not_b:
    for i in lines_a:
        if i not in lines_b:
            a_not_b.write(i)

with open('b_not_a.txt', 'w') as b_not_a:
    for i in lines_b:
        if i not in lines_a:
           b_not_a.write(i)