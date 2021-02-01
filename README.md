# Parking-Garage-Class

The goal of this personal project was to create a Parking Garage Class. Further description of this project can be found below.

The parking gargage class should have the following methods:

- takeTicket
   - This should decrease the amount of tickets available by 1
   - This should decrease the amount of parkingSpaces available by 1
- payForParking
   - Display an input that waits for an amount from the user and store it in a variable
   - If the payment variable is not empty then ->  display a message to the user that their ticket has been paid and they have 15mins to leave
   - This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
   - If the ticket has been paid, display a message of "Thank You, have a nice day"
   - If the ticket has not been paid, display an input prompt for payment
      - Once paid, display message "Thank you, have a nice day!"
   - Update parkingSpaces list to increase by 1
   - Update tickets list to increase by 1

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary