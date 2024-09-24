from my_time import timer






@timer
def test(count):
    list = []
    for i in range(count):
        list.append(i)
    return list

@timer
def test2(count):
    for i in range(count):
        yield i
@timer     
def unpuck(generator):
    list1 = list(generator)
    return list1
        
# test(100000000)
x = test2(100)

for i in x:
    if i == 50:
        print(i)
