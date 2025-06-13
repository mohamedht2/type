



parking_park =  {

"car park 1" : "",
"car park 2" : "",
"car park 3" : "",
"car park 4" : "",
"car park 5" : "YO05DLF"
}



def shows():

    print(parking_park)

def car_park():

    car_license_plate = input("enter your plate number for car")
    slot = input("enter car park slot")
    if len (car_license_plate) == 7:
        print("your plate number is" , car_license_plate)
    else:
        print("invalid try again")
        return
    parking_park.update ({slot:car_license_plate }) 

    while True:
        conformation = input("press Y to conutiune :   press N to return ")
        if conformation == "Y":
            print("")
        else:
            break



def car_removal ():
    
    amount_hours = int(input("enter amount of hours in min----------"))
    total_spend_time = cost_duration(amount_hours)
    print(total_spend_time)

    slot = int(input("enter slot number---------"))
    parking_park.update = ({slot : ""})




def cost_duration (total_spend_time):
    if total_spend_time < 60 :
        cost_time = 20
    else:
        cost_time = 10 + 2
    return(cost_time)
