if __name__ == "__main__":

    # Lambda as function
    sq = lambda x : x * x
    
    y = 7
    print(f"Square of {y} = {sq(y)}")


    # Lambda as anonymous function
    print(f"Cube of {y} = {(lambda x: x ** 3)(y)}")