if __name__ == "__main__":
    li = [1, 4, 6, 5, 8]
    li_iter = iter(li)

    print(li_iter)

    print(next(li_iter))
    print(next(li_iter))
    print(next(li_iter))
    print(next(li_iter))
    print(next(li_iter))
    # print(next(li_iter)) # raises error