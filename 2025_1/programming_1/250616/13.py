def bar(*b, **kwargs):
    if len(b) == 3:
        pass
    elif len(b) == 4:
        pass
    else:
        print("error")
        return
    
    print(b)
    print(kwargs)

foo = [val for val in range(1, 10)]
pos = {'d' : 10, 'e' : 20, 'f' : 30}