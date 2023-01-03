def generate_rug(n):
    if n % 2 == 0:
        return "the input number must be odd."
    rug = [[0]]
    counter = 0
    for i in range(1, int(n/2)+1):
        for row in rug:
            row.append(i)
            row.insert(0, i)
        rug.insert(0, [i for j in range(i+2+counter)])
        rug.append([i for j in range(i+2+counter)])
        counter += 1
    return rug

def print_rug(rug):
    for row in rug:
        for col in row:
            print(col, end="")
        print()

##### TEST CASE #####
print("When n = 7:")
print_rug(generate_rug(7))
