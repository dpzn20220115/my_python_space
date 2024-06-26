from functools import reduce
def do_it():
    pass


"""
1. for循环的其他替代方法
1.1 列表生成器
1.2 内置的map方法
1.3 内置的filter方法
1.4 reduce 方法
"""


def list_used_for():
    """列表生成器"""
    name = ["小明", "东东", "妮妮", "danny", "pengpeng"]
    list1 = [i for i in name]
    print(list1)


def filter_for():
    """filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
    该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中"""
    def len_str(n):
        return len(n) > 2
    new_list = filter(len_str, ["小明", "东东", "妮妮", "danny", "pengpeng"])
    print(list(new_list))

def map_for():
    """类似于filter,但两者不同，filter返回满足条件的元素，而map迭代并处理每个元素"""
    m = [6, 2, 3, 7, 1]
    squre = map(lambda x:x**2, m)
    print(list(squre))

def reduce_for():
    """
    前两个参数传给函数参数后，返回值与第三个继续执行，依次类推
    """

    def add(a, b):
        return a + b
    m = reduce(add, [1, 3, 6, 20, 3])
    print(m)
