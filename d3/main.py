ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
weight = dict(zip(ascii_lowercase + ascii_uppercase, range(1, 53)))
intersections = []
counts = []

with open('input') as data:
    for rp in data:
        rp_total = len(rp.strip())
        comparement_first = rp[:rp_total//2]
        comparement_second = rp[rp_total//2:]
        rp_intersection = list(set(comparement_first) & set(comparement_second))
        intersections += rp_intersection
        for i in rp_intersection:
            counts.append(weight[i])

print(counts, sum(counts))
