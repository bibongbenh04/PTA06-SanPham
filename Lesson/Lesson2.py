class Xe:
    def __init__(self, _hx = "Chua biet", _scn = "Chua biet", _ms = "Chua biet"):
        self.hangxe = _hx
        self.sochongoi = _scn
        self.mausac = _ms
    # ham de show ra thong tin cua lop
    def show(self):
        # ham duoc dung san de in ra tat ca thuoc tinh co trong class
        print(self.__dict__)


# Truong hop chua truyen tham so vao
xe1 = Xe()
xe1.show()

# Truong hop minh truyen tham so vao 
xe2 = Xe("Vinfast")
xe2.show()

xe3 = Xe("Vinfast", 2)
xe3.show()

xe4 = Xe("Vinfast", 2, "Trang")
xe4.show()
