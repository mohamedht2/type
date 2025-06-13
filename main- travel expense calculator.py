origin = input("Enter your origin ---- ")
destination = input("Enter your destunation ----  ")
num_day = int(input("Enter number of days ---- "))
User_budget = float(input("Enter total budget ----  "))
print(origin , "To" , destination , "<---->  number of days" , num_day , "<---->   And budget is" , User_budget)    


accommodation = print("""
    
    1- Standard --- £100
    2- Luxury ----- £200 
    3- budget ----  £50
 """)    


cho_acommodation =input("enter amount")


food = print("""

    select one 

    1- Standard ---- £40
    2- Luxury ---- £70
    3- Budget ----- £20

 """)

cho_food = input("enter amount ")

transport = print("""
    select one 
                  
    1- Public ---- £10 
    2- Rental Car ---- £50 
 """)

cho_tranport = input("enter amount")

activities = int(input("enter number of day of activities you want to do"))

total_activities = (activities * 30 )
total_acommodation = (cho_acommodation * num_day)
total_food = (cho_food * num_day )
total_transport = (cho_tranport * num_day)
estimated_cost = (User_budget - total_acommodation - total_food - total_transport - activities)

print("---------------------------------------------------------------")

print("destination :" , origin)
print("Number of Days :" , destination)
print("Budget :" , User_budget)
print("---------------------------------")
print("Estimated Cost")
print("Accommodation :" , total_acommodation )
print("Food :" , total_food)
print("transport :" , total_transport)
print("activities :" , activities)
print("--------------------------------------------------------")
print("total estimated cost: " , estimated_cost)












