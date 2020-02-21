a = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
b ={'A': 0, 'O': 0, 'B': 0, 'AB': 0}
b_key=list(b.keys())

for i in a:
    for j in range(0,len(b_key)):
        if i == b_key[j]:
            b[i] += 1

print(b)