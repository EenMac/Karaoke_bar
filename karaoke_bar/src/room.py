class Room:
    def __init__(self, number, name):
        self.number= number
        self.name = name
        self.songList = songList[7]
        self.room1 = []
        self.room2 = []
        # self.room_capacity =  room_capacity[8]

    def check_in(self, guest):
        self.room1.append(guest)

    def check_out(self, guest):
        self.room1.remove(guest)

    def add_song(self, song):
        self.songList.append(song)
        
    # def room_count(self):
    #     return len(self.guest)
    
    # def test_room_capacity(self):
    #     if room_count <= self.room_capacity:
    #         return "open for business"

    #     return "too many people"     

