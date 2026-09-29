#Generator#
def main():
    yield 1
    yield 2
    yield 3
res=main()
print(next(res))
print(next(res))
print(next(res))
