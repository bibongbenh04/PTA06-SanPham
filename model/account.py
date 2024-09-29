class Account:
    # ham khoi tao -> khi minh tao ra mot doi tuong moi
    def __init__(self, _un = "taikhoan", _pw = "123"):
        self.username = _un
        self.password = _pw
        self.loadDataFromFile()
    # ham in ra thong tin cua tai khoan
    def show(self):
        print(self.__dict__)
    # ham luu thong tin tu file
    def saveDataToFile(self):
        # mo file duoi dang viet
        with open("Data/account.txt", "w") as file:
            data = ""
            data += self.username + ","
            data += self.password
            # ghi vao file
            file.write(data)
    # ham doc thong tin tu file
    def loadDataFromFile(self):
        # mo file duoi dang doc
        with open("Data/account.txt", "r") as file:
            # doc het tat ca cac dong
            data = str(file.readline())
            # chia du lieu vao tung thuoc tinh
            self.username, self.password= data.split(",")
    # ham doi mat khau
    def changePassword(self, newPassword):
        self.password = newPassword
        self.saveDataToFile()
    # ham kiem tra dang nhap
    def checkAccount(self, _un, _pw):
        if _un == self.username and _pw == self.password:
            print("Dung thong tin")
        else:
            print("Sai thong tin")

ac1 = Account()
ac1.show()
ac1.changePassword("1234554321")
ac1.checkAccount("taikhoan", "1234554321")