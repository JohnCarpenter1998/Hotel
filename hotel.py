class Hotel:
    def __init__(self, name, address, floorCount, floorRatio):
        self.name = name
        self.address = address
        self.rooms = []
        for floor in range(floorCount):
            self.rooms.append([])
            for room in range(floorRatio):
                self.rooms[floor].append("")