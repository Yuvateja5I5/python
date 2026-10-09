class A:
    def disp_a(self):
        print("Inside A")
class B(A):
    def disp_b(self):
        Print("Inside B")
b1=B()
b1.disp_a()
b1.disp_b()
