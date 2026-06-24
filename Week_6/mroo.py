class A:
    def pr(self):
        # super().pr()
        print("A",end = '')

class X:
    def pr(self):
        # super().pr()
        print("X",end = '')

class B(A):
    def pr(self):
        super().pr()
        print("B",end = '')

class C(X):
# class C(A,X):
    def pr(self):
        super().pr()
        print("C",end = '')

class D(B,C):
    def pr(self):
        super().pr()
        print("D",end = '')

d = D()
d.pr()
print("\n",D.mro())




