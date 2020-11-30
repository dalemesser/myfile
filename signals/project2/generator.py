def square_number(n):
    result = []
    for i in n:
        result.append(i*i)
    return result

my_num = square_number([1,2,3,4,5])
print(my_num)

def squar_number_2(n):
    for i in n :
        yield (i*i)

num = squar_number_2([1,2,3,4,5])
print(next(num))
print(next(num))

numbers = [x*x for x in [1,2,3,4,5]]
print(numbers)

numbers_2 = list((x*x for x in [1,2,3,4,5]))
print(numbers_2)