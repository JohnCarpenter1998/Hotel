class Hotel:
    def __init__(self, name, address, floorCount, floorRatio):
        self.name = name
        self.address = address
        self.rooms = []
        self.guests = {}
        for floor in range(floorCount):
            self.rooms.append([])
            for room in range(floorRatio):
                self.rooms[floor].append("")

    def BookReservation(self, name,roomNumber):
        floor, roomIndex = self.convertNumberToRoom(roomNumber)
        if not self.validateRoomNumber(floor,roomIndex):
            print("Invalid room number")
            return
        self.rooms[floor][roomIndex] = name
        self.guests[name] = roomNumber

    def CancelReservation(self,name):
        roomNumber = self.guests[name]
        if roomNumber == False:
            print("Guest " + name + " Has no Reservation")
            return
        floor, roomIndex = self.convertNumberToRoom(roomNumber)
        self.rooms[floor][roomIndex] = ""
        self.guests[name] = False
        print("Reservation for " + name + " under room " + str(roomNumber) + " has been canceled")

    def SeeReservation(self, name):
        roomNumber = self.guests[name]
        if roomNumber == False:
            print("Guest " + name + " Has no Reservation")
            return
        floor, roomIndex = self.convertNumberToRoom(roomNumber)
        print(name + " Is staying in room " + str(roomNumber) + "." )

    def convertNumberToRoom(self, roomNumber):
        roomstr = str(roomNumber)
        floor = int(roomstr[0])
        roomIndex = int(roomstr[1:3])
        return floor, roomIndex

    def validateRoomNumber(self,floor,roomIndex):
        if floor >= 0 and floor < len(self.rooms) and roomIndex >= 0 and roomIndex < len(self.rooms[floor]):
            return True
        else:
            return False



