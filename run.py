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

data = pizzas.get_all_values()
#print(data)
# Function to print welcome messages
def print_welcome_messages():
    
    welcome_message1 = """
    ₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿
    ₿₿██████₿₿█████₿₿████████₿₿█████₿₿₿██████╗██₿₿₿██╗██╗░██████₿₿₿₿█████₿₿██₿₿₿₿██╗███████╗███₿₿₿██₿
    ₿██₿₿₿₿₿₿██╔══██₿₿₿₿██₿₿₿₿██╔══██╗██₿₿₿₿₿₿██₿₿₿██║██║██₿₿₿₿₿₿₿₿██₿₿₿██╗██₿₿₿₿██║██₿₿₿₿₿╝███₿₿₿██₿
    ₿₿█████₿₿███████₿₿₿₿██₿₿₿₿██║░░██₿₿█████₿₿███████║██║╚█████₿₿₿₿██₿₿₿██₿₿██₿₿██₿₿█████₿₿₿██₿██₿██₿
    ₿₿₿₿₿₿██╗██╔══██₿₿₿₿██₿₿₿₿██║░░██₿₿₿₿₿₿██╗██₿₿₿██║██║₿₿₿₿₿██₿₿₿██₿₿₿██₿₿₿████₿₿₿██₿₿₿₿₿₿██₿₿████₿
    ₿██████₿₿██║░░██₿₿₿₿██₿₿₿₿₿█████₿₿██████₿₿██₿₿₿██║██║██████₿₿₿₿₿█████₿₿₿₿₿██₿₿₿₿███████╗██₿₿₿███₿
    ₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿                   
    """
    welcome_message2 = """
    Greetings from Satoshi's Oven, where tradition bakes with innovation. 
    Our pizzas are a tribute to the spirit of Satoshi Nakamoto, 
    blending classic flavors with the modern twist of cryptocurrency payments. 
    Perfect for the crypto-curious and the digital devotee alike, 
    Satoshi's Oven offers a warm welcome to all who seek delicious pizza and a slice of digital freedom.
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
    print("\nPlease choose your preferred pizza from the menu by entering the corresponding code")
    print("\nMenu of Pizzas:")
    pizza_data = pizzas.get_all_values()
    for row in pizza_data[1:]:
        code, name, ingredients = row[:3] 
        print(f"{code}. {name} - Ingredients: {ingredients}")

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

def main():
    print_welcome_messages()
    user_choice = choose_option()
    if user_choice == '1':
        print("Starting a new order...")
        new_code = generate_order_code()

        
        print(f"Your order code is:  {new_code}. Please proceed with your order.")

        addresses = get_address_options()
        print("Available addresses for collection:\n")
        for code, address in addresses.items():
            print(f"{code}. {address}")

        while True:
            address_choice = input("Please enter the code for collection address:")
            if address_choice in addresses:
                selected_address = addresses[address_choice]
                print(f"You selected: {selected_address}\n")
                break
            else:
                print("Invalid address code selected. Please try again./n")

        print_pizza_menu()

        pizza_data = pizzas.get_all_values()
        pizza_dict = {row[0]: row[1:] for row in pizza_data[1:]} 
        while True:
            pizza_choice = input("Please enter the code for your chosen pizza: ")
            if pizza_choice in pizza_dict:
                selected_pizza = pizza_dict[pizza_choice]
                print(f"You have selected: {selected_pizza[0]} - {selected_pizza[1]}")
                break  
            else:
                print("Invalid pizza code selected. Please try again.")
        

        sizes_dict = get_pizza_sizes()
        print_pizza_sizes(sizes_dict)
        size_choice = input("Please enter R or L code for your chosen size: ")
        while size_choice not in sizes_dict:
            print("Invalid size code selected. Please try again.")
            size_choice = input("Please enter R or L code for your chosen size: ")
        selected_size = sizes_dict[size_choice]
        print(f"You have selected: {selected_size['Size']} - Price: {selected_size['Price']}")
        
        # Cheese selection logic
        cheese_options = get_cheese_options()
        print_cheese_options(cheese_options)
        while True:
            cheese_choice = input("Please enter the code for your chosen cheese option: ")
            if cheese_choice in cheese_options:
                selected_cheese = cheese_options[cheese_choice]
                print(f"You have selected: {selected_cheese}")
                break
            else:
                print("Invalid cheese code selected. Please try again.")
        
        orders_row = new_code 
        
        orders.append_row([new_code, selected_address, selected_pizza[0], selected_pizza[1], selected_size['Size'], selected_cheese, "", "", selected_size['Price']])


    elif user_choice == '2':
        print("Checking order status...")
if __name__ == "__main__":
    main()

