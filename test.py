import itertools

# 变量输入
inputList = [0,1,2,{"a":1,"b":2},"b","c"]

resultList = []
for index in range(len(inputList)):
    combinations = list(itertools.combinations(inputList, index+1))
    for combination in combinations:
        resultList.append(combination)

print(resultList)

# 假设我们处理的结果为：[(0,), (1,), (2,), ('a',), ('b',), ('c',), (0, 1), (0, 2), (0, 'a'), (0, 'b'), (0, 'c'), (1, 2), (1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), ('a', 'b'), ('a', 'c'), ('b', 'c'), (0, 1, 2), (0, 1, 'a'), (0, 1, 'b'), (0, 1, 'c'), (0, 2, 'a'), (0, 2, 'b'), (0, 2, 'c'), (0, 'a', 'b'), (0, 'a', 'c'), (0, 'b', 'c'), (1, 2, 'a'), (1, 2, 'b'), (1, 2, 'c'), (1, 'a', 'b'), (1, 'a', 'c'), (1, 'b', 'c'), (2, 'a', 'b'), (2, 'a', 'c'), (2, 'b', 'c'), ('a', 'b', 'c'), (0, 1, 2, 'a'), (0, 1, 2, 'b'), (0, 1, 2, 'c'), (0, 1, 'a', 'b'), (0, 1, 'a', 'c'), (0, 1, 'b', 'c'), (0, 2, 'a', 'b'), (0, 2, 'a', 'c'), (0, 2, 'b', 'c'), (0, 'a', 'b', 'c'), (1, 2, 'a', 'b'), (1, 2, 'a', 'c'), (1, 2, 'b', 'c'), (1, 'a', 'b', 'c'), (2, 'a', 'b', 'c'), (0, 1, 2, 'a', 'b'), (0, 1, 2, 'a', 'c'), (0, 1, 2, 'b', 'c'), (0, 1, 'a', 'b', 'c'), (0, 2, 'a', 'b', 'c'), (1, 2, 'a', 'b', 'c'), (0, 1, 2, 'a', 'b', 'c')]
returnList = []

# 穷举所有
def dynamic_fn(*args):
    if args.count == 1:
        return args[0]
    if args.count == 2:
        return args[0] and args[1]

for rels in resultList:
    dynamic_fn(rels)
