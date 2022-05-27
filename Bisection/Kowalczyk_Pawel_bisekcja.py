
def function(x):
    return x*x*x - x -2

def kowalczyk_pawel_bisekcja(a, b, eps):
    c = (a+b)/2
    if (b - a) <= eps:
        return c
    else:
        while (b - a) > eps:
            if function(a)*function(c) < 0:
                b = c
                c = (a+b)/2
            else:
                a = c
                c = (a+b)/2
        return c

print(kowalczyk_pawel_bisekcja(1,2, 0.0001))