class A:
    def disp_a(self):
        print("Inside A")
class B(A):
    def disp_b(self):
        print("Inside B")
class c(B):
    def disp_c(self):
        print("Inside C")
c1=c()
c1.disp_c()
c1.disp_b()
c1.disp_a()
