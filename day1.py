f = sorted(eval(open("input.txt").read().
    replace('\n\n', ',').replace('\n', '+')))

print(f[-1], sum(f[-3:]))


#
# 
# var = open('input.txt','r').read().split("\n\n")
#total_kcal = []

#for line in var:
#    total_kcal.append(sum([int(i) for i in line.split("\n")]))
#print(max(total_kcal))
