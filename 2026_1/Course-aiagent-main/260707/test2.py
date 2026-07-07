# [컴플리현션] # list, string
bar = [value for value in range(1, 10 + 1, 2)
       if value % 3 == 0]
print(bar)
# {컴플리현션} # dict, set
text = ["a", "abc", "ef"]
foo = {value:len(value) for value in text}
print(foo)