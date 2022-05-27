
def Kowalczyk_Pawel_Lagrange(x, xw, yw, n):
    # n - degree of a polynomial; xw,yw - nodes of the polynomial
    total = 0
    for i in range(0, n+1):
        product = 1
        for j in range(0, n+1):
            if j != i:
                product = product * (x-xw[j])/(xw[i]-xw[j])
        total = total + product*yw[i]
    return total


xw = [-2, 1, 4]
yw = [5, 3, 7]
x = 5
n = 2
print(Kowalczyk_Pawel_Lagrange(x, xw, yw, 2))