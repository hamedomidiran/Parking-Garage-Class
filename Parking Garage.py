

from IPython.display import clear_output as co

class ParkingGarage:
    def __init__(self):
        self.tickets       = [num for num in range(1,101)]
        self.parkingSpaces = [num for num in range(1,101)]
        self.parkingdir    = {}
        self.currentTicket = {}
    
    
    def takeTicket(self):
        co()
        plate_number       = input("Please type in your plate number:       ")
        if plate_number.upper() in self.parkingdir:
            print('\nYou already have a ticket.')
            return self.tickets, self.parkingSpaces, self.parkingdir
        else:
            users_ticket       = self.tickets[0]
            self.parkingdir.update({plate_number.upper() : {'Paid' : False, 'Ticket Number' : users_ticket}})
            self.tickets.remove(users_ticket)
            self.parkingSpaces.remove(users_ticket)
            co()
            print("Thank you. Kindly take your ticket and park in any spot.")
            return self.tickets, self.parkingSpaces, self.parkingdir
        
    def payforParking(self):
        co()
        plate_number       = input("Please type in your plate number:       ")
        
        if plate_number.upper() in self.parkingdir:
            co()
            payment  = input('How much would you like to pay: $')
            
            while str(payment) == "":
                co()
                print('Please type in an amount')
                payment  = input('How much would you like to pay: $')
                
            for key, value in self.parkingdir.items():
                if key == plate_number.upper():
                    current_dict = {key: value}
                    current_dict[key]['Paid'] = True

                    key = current_dict
                    co()
                    print('Your ticket has been paid. You have 15 minutes to leave. Thank you')
            
            return self.parkingdir
        
        else:
            co()
            print("You currently don't have a ticket.")
            return self.parkingdir
        


            
    def leaveGarage(self):
        co()
        plate_number       = input("Please type in your plate number:       ")
        if plate_number.upper() in self.parkingdir:
            
            for key, value in self.parkingdir.items():
                if key == plate_number.upper():
                    current_dict = {key: value}
                    if current_dict[key]['Paid'] == True:
                        co()
                        print('Thank You, have a nice day.')
                        ticket_no = self.parkingdir[key]['Ticket Number']
                        self.tickets.append(ticket_no)
                        self.parkingSpaces.append(ticket_no)
                        del self.parkingdir[key]
                        return self.tickets, self.parkingSpaces, self.parkingdir
                    else:
                        co()
                        print('You have not paid for Parking.')
                        return self.tickets, self.parkingSpaces, self.parkingdir
                        
        else:
            co()
            print('Have a nice day.')
            return self.tickets, self.parkingSpaces, self.parkingdir
            
            
            
        
def run_PG_simulation():
    ParkingGarage1  = ParkingGarage()
    tickets         = ParkingGarage1.tickets
    parking_spaces  = ParkingGarage1.parkingSpaces
    parking_dir     = ParkingGarage1.parkingdir
    
    while True:
        co()
        to_start = input('Press Enter to start: ')
        while ParkingGarage1.tickets != []:
            co()
            print('\nWelcome to the stall. Please select one of the 3 options')
            driver_input = input(' Type 1 to Get Ticket \n Type 2 to Pay for Parking \n Type 3 to leave the garage \n'
                                 ' Type 4 to quit \n')

            while int(driver_input) != 1 and int(driver_input) != 2 and int(driver_input) != 3 and int(driver_input) != 4:
                co()
                print('\nSorry, that is not an option.')
                driver_input = input('Type 1 to Get Ticket \n Type 2 to Pay for Parking \n Type 3 to leave the garage \n'
                                 ' Type 4 to quit \n')


            if int(driver_input) == 1:
                tickets, parking_spaces, parking_dir = ParkingGarage1.takeTicket()
                input('\nPress Enter go back to the main menu')


            if int(driver_input) == 2:
                parking_dir = ParkingGarage1.payforParking()
                input('\nPress Enter go back to the main menu')


            if int(driver_input) == 3:       
                tickets, parking_spaces, parking_dir = ParkingGarage1.leaveGarage()
                input('\nPress Enter go back to the main menu')


            if int(driver_input) == 4:
                co()
                print('Thank you. Have a nice day')
                break

    

            
run_PG_simulation()
        
        
        