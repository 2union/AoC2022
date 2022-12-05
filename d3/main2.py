ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
weight = dict(zip(ascii_lowercase + ascii_uppercase, range(1, 53)))
intersections = []
counts = []

group = 3
count = 1
group_rps = []
with open('input') as data:
    for rp in data:
        group_rps.append(set(rp.strip()))
        if count%group == 0:
            rp1, rp2, rp3 = group_rps[-3:]
            intersection = rp1 & rp2 & rp3
            intersections += rp1, rp2, rp3
            for i in intersection:
                print(i)
                counts.append(weight[i])
        count += 1

print(counts, sum(counts))
