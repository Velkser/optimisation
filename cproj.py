import cProfile

def my_function():
    total = 0
    for i in range(1000000):
        total += i
        
    for j in range(100000000):
        total += i
        
    for j in range(1000):
        total *= i
    return total

def my_function2():
    total = 0
    for i in range(1000000):
        total += i
    return total

cProfile.run('my_function()')
cProfile.run('my_function2()')