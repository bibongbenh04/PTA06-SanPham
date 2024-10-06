import webbrowser

class Music:
    def __init__(self, _l, _n, _a, _s, _d):
        self.link = _l
        self.name = _n
        self.artist = _a
        self.stream = _s
        self.duration = _d
    # ham de mo bai hat
    def open(self):
        webbrowser.open(self.link)

listmusics = []
# lay link tu youtube
ms1 = Music("https://www.youtube.com/watch?v=3UbQjlHbPsE", "NHỮNG KẺ MỘNG MƠ - LIÊN MINH TINH TÚ | CÔNG DIỄN 2 ANH TRAI VƯỢT NGÀN CHÔNG GAI 2024", "Anh Trai Vuot Ngan Chong Gai", "3,102,121 views", "5:30s")
listmusics.append(ms1)
# ms1.open()
# lay link tu spotify
ms2 = Music("https://open.spotify.com/track/3ztP5O7dJSha2PG429eUCb?si=cdab0ffb84fa4c27", "Thien Ly Oi", "Jack-J97", "4.700.700", "3:40")
listmusics.append(ms2)
# ms2.open()
# mo bai hat co trong may tinh ca nhan
ms3 = Music("D:\BiBongBenh\Downloads\y2meta.com - nhạc chill mà kira hay dùng (320 kbps).mp3", "Chua biet", "Chua Biet", "Chua Biet", "Chua Biet")
listmusics.append(ms3)

listmusics[1].open()

