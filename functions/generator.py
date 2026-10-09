#Generator#
def main():
    yield 1
    yield 2
    yield 3
res=main()#creation of object
print(res)#it prints generator address
print(next(res))
print(next(res))
print(next(res))
