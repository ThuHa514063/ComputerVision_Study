from scipy import optimize

def f(x):
    return x**2 + 3*x + 2

result = optimize.minimize(f, x0=0)

print(result.x)