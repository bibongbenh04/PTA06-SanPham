class Person:
    # ham khoi tao -> khi minh tao ra mot doi tuong moi
    def __init__(self, _cP, _aP, fn, nn, bt, rl, ed):
        self.coverPicture = _cP
        self.avatarPicture = _aP
        self.fullname = fn
        self.nickname = nn
        self.birthdate = bt
        self.relationship = rl 
        self.education = ed
    # ham in ra thong tin cua nguoi do
    def show(self):
        print(self.__dict__)
    # ham luu thong tin tu file
    def saveDataToFile(self):
        # mo file duoi dang viet
        with open("Data/person.txt", "w") as file:
            data = ""
            data += self.coverPicture + ","
            data += self.avatarPicture + ","
            data += self.fullname + ","
            data += self.nickname + ","
            data += self.birthdate + ","
            data += self.relationship + ","
            data += self.education
            # ghi vao file
            file.write(data)
    # ham doc thong tin tu file
    def loadDataFromFile(self):
        # mo file duoi dang doc
        with open("Data/person.txt", "r") as file:
            # doc het tat ca cac dong
            data = str(file.readline())
            # chia du lieu vao tung thuoc tinh
            self.coverPicture, self.avatarPicture, self.fullname, self.nickname, self.birthdate, self.relationship, self.education = data.split(",")


ps1 = Person("null", "null", "Le Hong Quan", "Bibongbenh", "29/10/2004", "Unknown", "HCMUE")
ps1.loadDataFromFile()
ps1.show()
# ps1.saveDataToFile()