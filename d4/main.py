with open('input') as f:
    count = 0
    for i in f:
        e1, e2 = i.strip().split(',')
        e1_b, e1_e = map(int, e1.split('-'))
        e2_b, e2_e = map(int, e2.split('-'))
        if (e1_b <= e2_b and e1_e >= e2_e) or (e2_b <= e1_b and e2_e >= e1_e):
            count += 1

print(count)
