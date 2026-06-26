def bar(args):
    print(args[0])
    print(args)

#[2, 4, 6, 8, 10]
arg_1 = [val for val in range(2, 11, 2)]
#[1, 3, 5, 7, 9]
arg_2 = [val for val in range(1, 11, 2)]

#print(*arg_1)
#print(*arg_2)
bar(*arg_1)
bar(*arg_2)