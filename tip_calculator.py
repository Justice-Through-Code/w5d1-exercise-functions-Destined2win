# tip_calculator.py
def tip_calculator():
# TODO: Create a function named calculate_tip
 try:  #DO NOT MODIFY
     


    # TODO:
        # Get these user inputs
    
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
        total_cost = float(input('What is the cost of the meal without tax? '))
        num_people = int(input('The number of people splitting the bill?' ))
        tip_percentage = float(input('Enter tip percentage ')) / 100

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).
        percentage_sales_tax = 0.10
        sales_tax = total_cost * percentage_sales_tax
        total_bill = total_cost + sales_tax + (total_cost * tip_percentage)


        

    # NOTE: Calculate the tip and tax separately. 
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
        amount_per_person = total_bill / num_people
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00
        print(f'Total bill: ${total_bill:.2f}')
        print(f'Each person should pay: ${amount_per_person:.2f}')    
    
    # NOTE: The amounts are displayed with 2 decimals only
        # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid 


 except ValueError:
     print("Invalid input. Please enter valid numbers for cost, number of people, and tip percentage.")

       
    
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY
