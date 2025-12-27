if __name__ == "__main__":
    li = [1, 4, 6, 5, 8]
    li_iter = iter(li)

    print(li_iter)

    for el in li_iter:
        print(el)