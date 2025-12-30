# Diamond Problem in Python
# In this example, class D inherits from both B and C, which in turn inherit from A.
# Both B and C override the show method from A. When we call show on an instance of D,
# Python uses the Method Resolution Order (MRO) to determine which show method to
# invoke. In this case, it will call B's show method because B appears before C in D's MRO.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()

print(D.mro())  # Method Resolution Order