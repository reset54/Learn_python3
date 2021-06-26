def f():
    return [43, 65, 32]

def genf():
    s = 7
    for i in [43, 65, 32]:
        yield i
        print(s)
        s = s * 10 + 7

g = genf()

print(f"Step 1 out: {next(g)}")
print(f"Step 2 out: {next(g)}")
print(f"Step 3 out: {next(g)}")


# https://youtu.be/8cMMO8fks-k
# https://youtu.be/vn6bV6BYm7w
 
# 1
def fact(n):
    pr = 1
    a = []
    for i in range (1, n+1):
        pr = pr*i
        a.append(pr)
    return a

print(fact(15))
print()

# 2
def fact_gen(n):
    pr = 1
    for i in range (1, n+1):
        pr = pr * i
        yield pr


s = fact_gen(10)
print(f"Step 1 out: {next(s)}")
print(f"Step 2 out: {next(s)}")
print(f"Step 3 out: {next(s)}")


for i in fact(15):
    print(i, end = "-,-")