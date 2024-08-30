kmDistance = float(input("Enter the distance in KM: "))
shortKmTicketPrice = 0.5
longKmTicketPrice = 0.45

if kmDistance <= 200:
    ticketPrice = kmDistance * shortKmTicketPrice
    print(f"The Ticket value is: ${ticketPrice:6.2f}")
else:
    ticketPrice = kmDistance * longKmTicketPrice
    print(f"The Ticket value is: ${ticketPrice:6.2f}")