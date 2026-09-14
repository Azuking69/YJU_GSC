class tv:
    ...

class dvd:
    ...

class tvdvd(tv, dvd):
    ...

class A:
    ...

class B(object):
    ...

print(A.mro())
print(B.mro())