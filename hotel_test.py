from hotel import Hotel

hotel = Hotel("Holiday Inn","16 Wolf Road", 3, 20)
print(hotel.name)
hotel.BookReservation("John", 205)
hotel.SeeReservation(205)
hotel.SeeReservation(115)
hotel.CancelReservation(205)
hotel.SeeReservation(205)
hotel.BookReservation("John", 305)
hotel.CancelReservation(265)
hotel.CancelReservation(201)

