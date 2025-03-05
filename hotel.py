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
        floor, roomIndex = self.convertNumberToRoom(roomNumber)
        if not self.validateRoomNumber(floor,roomIndex):
            print("Invalid room number")
            return
        self.rooms[floor][roomIndex] = name

    def CancelReservation(self,roomNumber):
        floor, roomIndex = self.convertNumberToRoom(roomNumber)
        if not self.validateRoomNumber(floor,roomIndex):
            print("Invalid room number")
            return
        name = self.rooms[floor][roomIndex]
        self.rooms[floor][roomIndex] = ""
        print("Reservation for " + name + " under room " + str(roomNumber) + " has been canceled")

    def SeeReservation(self, roomNumber):
        floor, roomIndex = self.convertNumberToRoom(roomNumber)
        if not self.validateRoomNumber(floor,roomIndex):
            print("Invalid room number")
            return
        if self.rooms[floor][roomIndex] != "":
            print(self.rooms[floor][roomIndex] + " Is staying in room " + str(roomNumber) + "." )
        else:
            print("Room " + str(roomNumber) + " is vacant.")

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



