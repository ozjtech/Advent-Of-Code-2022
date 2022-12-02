var = open(0,'r').read().split("\n\n")
total_kcal = []

for line in var:
    total_kcal.append(sum([int(i) for i in line.split("\n")]))

print(max(total_kcal))
print(sum(sorted((total_kcal))[-3:]))