def methodcaption(another):
    return another()


def add_two_numbers():
    return 35 + 77


# print(methodcaption(add_two_numbers))

print(methodcaption(lambda:35 + 77))

my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x > 13, my_list)))


(lambda x: x * 3)(5)

def f(x):
    return x * 3

f(5)

def gt_thirteen(x):
    return x > 13

print(list(filter(gt_thirteen , my_list)))
print([x for x in my_list if x > 13])