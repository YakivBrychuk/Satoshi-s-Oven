import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_file('creds.json', scopes=SCOPES)
client = gspread.authorize(creds)

sheet = client.open('satoshis_oven')
pizzas = sheet.worksheet('pizzas')
address = sheet.worksheet('address')
orders = sheet.worksheet('orders')
sizes = sheet.worksheet('sizes')
cheese = sheet.worksheet('cheese')
toppings = sheet.worksheet('toppings')
payment_methods = sheet.worksheet('payment_method')

data = pizzas.get_all_values()

# Function to print welcome messages


def print_welcome_messages():

    welcome_message1 = """
    Welcome to Satoshi's Oven!₿🍕                                                             
    """
    welcome_message2 = """
    Greetings from Satoshi's Oven, where tradition bakes with innovation. 
    Our pizzas are a tribute to the spirit of Satoshi Nakamoto, 
    blending classic flavors with the modern twist of cryptocurrency payments. 
    Perfect for the crypto-curious and the digital devotee alike, 
    Satoshi's Oven offers a warm welcome to all 
    who seek delicious pizza and a slice of digital freedom.
    """
    print(welcome_message1, welcome_message2)

# Function to choose an option
def choose_option():
    while True:
        print("\nChoose an option:")
        print("1. Start a new order")
        print("2. Check the status of an existing order")
        
        user_choice = input("Enter your choice (1 or 2): ")
        
        if user_choice in ['1', '2']:
            return user_choice
        else:
            print("Invalid input. Please try again.\n")

# Function to generate a new order code
def generate_order_code():
    order_codes = orders.col_values(1)  
    numeric_codes = [int(code) for code in order_codes if code.isdigit()]
    last_order_code = max(numeric_codes, default=0)
    new_order_code = last_order_code + 1
    return new_order_code

# Function to get address options
def get_address_options():
    
    sheet = client.open('satoshis_oven')  
    address_sheet = sheet.worksheet('address')
    
    # Pull all data from the 'address' sheet
    address_data = address_sheet.get_all_values()
    
    # Create a dictionary of addresses
    addresses = {row[0]: row[1] for row in address_data[1:]}
      
    
    return addresses
    
    
print(get_address_options)


# Function to print the menu of pizzas
def print_pizza_menu():
    print("\nMenu of Pizzas:")
    pizza_data = pizzas.get_all_values()
    for row in pizza_data[1:]:
        code, name, ingredients = row[:3] 
        print(f"{code}. {name} - Ingredients: {ingredients}")
    print()  
    print("\nPlease choose your preferred pizza from the menu by entering the corresponding code")

# Function to get pizza sizes
def get_pizza_sizes():
    
    sizes_data = sizes.get_all_values()
    sizes_dict = {row[0]: {'Size': row[1], 'Price': row[2]} for row in sizes_data[1:]}
    return sizes_dict

# Function to print pizza sizes
def print_pizza_sizes(sizes_dict):
    print("Available Pizza Sizes:")
    for code, info in sizes_dict.items():
        print(f"{code}. {info['Size']} - Price: {info['Price']}")

# Function to get cheese options
def get_cheese_options():
    cheese_data = cheese.get_all_values()
    cheese_options = {row[0]: row[1] for row in cheese_data[1:]}  
    return cheese_options

# Function to print cheese options
def print_cheese_options(cheese_dict):
    print("Available Cheese Options:")
    for code, cheese_type in cheese_dict.items():
        print(f"{code}. {cheese_type}")

# Constants for additional costs


CHEESE_COST = 1.5
TOPPING_COST = 1.5


# Function to get toppings options
def get_toppings_options():
    toppings_data = toppings.get_all_values()
    toppings_options = {row[0]: row[1] for row in toppings_data[1:]} 
    return toppings_options

# Function to print toppings options
def print_toppings_options(toppings_dict):
    print("Available Toppings:")
    for code, topping in toppings_dict.items():
        print(f"{code}. {topping}")

# Function to get payment methods
def get_payment_methods():
    payment_methods_data = payment_methods.get_all_values()
    payment_options = {row[0]: {'Method': row[1], 'Symbol': row[2]} for row in payment_methods_data[1:]}
    return payment_options

# Function to print payment method options and to choose a payment method
def choose_payment_method():
    payment_options = get_payment_methods()
    print("\nAvailable Payment Methods:")
    for code, info in payment_options.items():
        print(f"{code}. {info['Method']} - {info['Symbol']}")

    print("\nPlease choose your preferred payment method by entering the corresponding code (C for Crypto, F for Fiat/Eur): ")
    while True:
        payment_choice = input().upper()
        if payment_choice in payment_options:
            selected_payment_method = payment_options[payment_choice]
            print(f"You have selected: {selected_payment_method['Symbol']}")
            return selected_payment_method
        else:
            print("Invalid payment method code selected. Please try again.")

# Function to check the status of an existing order
def check_order_status():
    order_number = input("Please input your order number: ")
    
    try:
        
        order = orders.find(order_number)
        order_row = orders.row_values(order.row)
        
        # Format and display the order details
        print("Here are the details of your order:")
        print(f"Order Number: {order_row[0]}")
        print(f"Address: {order_row[1]}")
        print(f"Pizza: {order_row[2]}")
        print(f"Ingredients: {order_row[3]}")
        print(f"Size: {order_row[4]}")
        print(f"Cheese: {order_row[5]}")
        print(f"Toppings: {order_row[6]}")
        print(f"Payment Method: {order_row[7]}")
        print(f"Total Price: {order_row[8]}")
        
    except Exception as e:
        if "CellNotFound" in str(e):
            print("You don't have access to this order or it doesn't exist.")
        else:
            print("You don't have access to this order or it doesn't exist.")

# Function to print order summary
def print_order_summary(new_code, selected_address, selected_pizza, selected_size, selected_cheese, selected_toppings_str, selected_payment_method, total_price):
    print("\nOrder Summary:")
    print(f"Order Number: {new_code}")
    print(f"Collection Address: {selected_address}")
    print(f"Pizza: {selected_pizza[0]}")
    print(f"Size: {selected_size['Size']}")
    print(f"Cheese: {selected_cheese}")
    print(f"Toppings: {selected_toppings_str}")
    print(f"Payment Method: {selected_payment_method['Method']}")
    print(f"Total Price: {total_price} {selected_payment_method['Symbol']}")
    print("\nPlease review your order. If everything is correct, type 'finish' to complete your order.")


# Function to update the order status
def update_order_status(row_number, status):
    
    status_column_index = 10
    
    orders.update_cell(row_number, status_column_index, status)
  

def main():
    print_welcome_messages()
    user_choice = choose_option()
    if user_choice == '1':
        total_price = 0
        print("Starting a new order...")
        new_code = generate_order_code()
        print(f"Your order code is: {new_code}. Please proceed with your order.")
        print()

        addresses = get_address_options()
        print("Available addresses for collection:\n")
          
        for code, address in addresses.items():
            print(f"{code}. {address}")

        print()
        while True:
            address_choice = input("Please enter the code for collection address:")
            if address_choice in addresses:
                selected_address = addresses[address_choice]
                print()
                print(f"You selected: {selected_address}\n")
                break
            else:
                print("Invalid address code selected. Please try again./n")

        print_pizza_menu()
        print()
        pizza_data = pizzas.get_all_values()
        pizza_dict = {row[0]: row[1:] for row in pizza_data[1:]} 
        while True:
            pizza_choice = input("Please enter the code for your chosen pizza: ")
            if pizza_choice in pizza_dict:
                selected_pizza = pizza_dict[pizza_choice]
                print(f"You selected: {selected_pizza[0]} - {selected_pizza[1]}")
                
                break  
            else:
                print("Invalid pizza code selected. Please try again.")
        
        print()
        sizes_dict = get_pizza_sizes()
        print_pizza_sizes(sizes_dict)
        print()
        size_choice = input("Please enter R or L code for your chosen size: ")
        
        if(size_choice == 'R' or size_choice == 'r'):
            size_choice = 'R'
        elif(size_choice == 'L' or size_choice == 'l'):
            size_choice = 'L'
        while size_choice not in sizes_dict:
            print("Invalid size code selected. Please try again.")
            size_choice = input("Please enter R or L code for your size: ")

        selected_size = sizes_dict[size_choice]
        total_price += float(selected_size['Price'])
        print()
        print(f"You selected: {selected_size['Size']} - {selected_size['Price']}")
        
        # Cheese selection logic
        cheese_options = get_cheese_options()
        print_cheese_options(cheese_options)
        print()
        while True:
            cheese_choice = input("Enter the code of your cheese option: ")
            if cheese_choice in cheese_options:
                selected_cheese = cheese_options[cheese_choice]
                print(f"You have selected: {selected_cheese}")
                if selected_cheese != "No cheese":
                    total_price += CHEESE_COST
                break
            else:
                print("Invalid cheese code selected. Please try again.")
        print()
        toppings_options = get_toppings_options()
        print_toppings_options(toppings_options)
        print()
        selected_toppings = []  # To store selected toppings
        while True:
            toppings_choice = input("Please enter the code for your chosen toppings (enter 'done' when finished): ")
            
            if toppings_choice.lower() == 'done' and selected_toppings:
                break
            elif toppings_choice == '0':  # If "No Toppings" is selected
                selected_toppings.append(toppings_options[toppings_choice])
                print(f"You have added: {toppings_options[toppings_choice]}")
                break  # Break after "No Toppings" is selected
            elif toppings_choice in toppings_options:
                selected_toppings.append(toppings_options[toppings_choice])
                print(f"You have added: {toppings_options[toppings_choice]}")
            else:
                print("Invalid toppings code selected. Please try again.")
        
        selected_toppings_str = ', '.join(selected_toppings)
        for topping in selected_toppings:
        # Add the TOPPING_COST for each selected topping
         total_price += TOPPING_COST

        selected_payment_method = choose_payment_method()
        print_order_summary(new_code, selected_address, selected_pizza, selected_size, selected_cheese, selected_toppings_str, selected_payment_method, total_price)
        print()
        # Prompt user to finish or edit the order
        order_data = [
        new_code, selected_address, selected_pizza[0], selected_pizza[1], 
        selected_size['Size'], selected_cheese, selected_toppings_str, 
        selected_payment_method['Method'], str(total_price), ""]
        orders.append_row(order_data)

        # After appending, the new order should be at the last row of the sheet
        number_of_rows = len(orders.get_all_values())

        while True:
            finish_choice = input("Type 'finish' to complete your order or 'edit' to make changes: ").lower()
            if finish_choice == 'finish':
                print("Thank you for your order! Your delicious pizza will be ready soon.")
                # Update the status for the new order row
                update_order_status(number_of_rows, "Processed")
                break
            elif finish_choice == 'edit':
                # Implement edit functionality if needed
                print("Edit functionality is not yet implemented.")
                update_order_status(number_of_rows, "Processed")
                print("Thank you for your order! Your delicious pizza will be ready soon.")
                break
            else:
                print("Invalid input. Please type 'finish' to complete your order or 'edit' to make changes.")

                print(f"Your total is: {total_price} {selected_payment_method['Symbol']}")
                
            orders_row = new_code 
    
    elif user_choice == '2':
        check_order_status()

    print()
    print("The order has been processed successfully!")
    print()
    print("The application is now closing. Thank you for using Satoshi's Oven.")
    print()
    print("We look forward to seeing you soon at the collection point. Enjoy your meal!")
    print()
    print("Goodbye!")
if __name__ == "__main__":
    main()




