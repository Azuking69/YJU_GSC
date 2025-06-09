"""
def 함수 (positional argument, variant argument, 
         keyword argument, variant keyword argument):
"""

def foo(**kwargs):
    print(kwargs)

foo(a=2, b=3, c=4)
foo(d=70, e=80, f=90, g=100)