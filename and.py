#simple implementation of artificial neural network for "AND"
#1 = true; 0 = false
x = []
def nett(input_x):
    val = 0
    for i in input_x:
        val += i * 1
    return val

for i in range(0,2):
    x.append(int(input()))

if nett(x) >= 2:
    print(1)
if nett(x) < 2:
    print(0)