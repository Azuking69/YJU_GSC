# 변수의 Scope와 lifetime

print(bar)
bar = "hello" # => Error 

bar = "hello"
print(bar) # => hello 출력

del bar
print(bar) # => Error (삭제)