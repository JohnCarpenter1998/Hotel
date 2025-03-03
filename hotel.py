class Hotel:
    def __init__(self, name, address, floorCount, floorRatio):
        self.name = name
        self.address = address
        self.rooms = []
        for floor in range(floorCount):
            self.rooms.append([])
            for room in range(floorRatio):
                self.rooms[floor].append("")

    def BookReservation(self, name,roomNumber):
        roomstr = str(roomNumber)
        floor = int(roomstr[0])
        roomIndex = int(roomstr[1:3])
        self.rooms[floor][roomIndex] = name


