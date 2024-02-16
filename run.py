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

data = pizzas.get_all_values()
print(data)
# Function to print welcome messages
def print_welcome_messages():
    
    welcome_message1 = """
    ₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿₿
    ₿₿██████╗░█████╗░████████╗░█████╗░░██████╗██╗░░██╗██╗░██████╗₿₿░█████╗░██₿₿₿₿██╗███████╗███₿₿₿██₿
    ₿██₿₿₿₿₿╝██╔══██╗╚══██╔══╝██╔══██╗██₿₿₿₿₿╝██║░░██║██║██₿₿₿₿₿╝₿₿██₿₿₿██╗██₿₿₿₿██║██₿₿₿₿₿╝███₿₿₿██₿
    ₿₿█████╗░███████║░░░██║░░░██║░░██║╚█████╗░███████║██║╚█████╗░₿₿██₿₿₿██║╚██₿₿██╔╝█████╗░░██₿██₿██₿
    ₿₿₿₿₿₿██╗██╔══██║░░░██║░░░██║░░██║₿₿₿₿₿██╗██╔══██║██║₿₿₿₿₿██╗₿₿██₿₿₿██║░╚████╔╝░██₿₿₿₿₿░██₿₿████₿
    ₿██████╔╝██║░░██║░░░██║░░░╚█████╔╝██████╔╝██║░░██║██║██████╔╝₿₿₿█████╔╝░░╚██╔╝░░███████╗██₿₿₿███₿
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
            print("Invalid input. Please try again./n")

# Function to generate a new order code
def generate_order_code():
    order_codes = orders.col_values(1)  
    numeric_codes = [int(code) for code in order_codes if code.isdigit()]
    last_order_code = max(numeric_codes, default=0)
    new_order_code = last_order_code + 1
    return new_order_code

# Function to get address options
def get_address_options():
    
    sheet = client.open('satoshis_oven')  # Open the spreadsheet
    address_sheet = sheet.worksheet('address')  # Access the 'address' worksheet
    
    # Pull all data from the 'address' sheet
    address_data = address_sheet.get_all_values()
    
    # Create a dictionary of addresses
    addresses = {row[0]: row[1] for row in address_data[1:]}
      
    
    return addresses
print(get_address_options)

def main():
    print_welcome_messages()
    user_choice = choose_option()
    if user_choice == '1':
        print("Starting a new order...")
        new_code = generate_order_code()

        # Write the new order code to the 'orders' sheet
        print(f"Your order code is:  {new_code}. Please proceed with your order.")

        addresses = get_address_options()
        print("Available addresses for collection:/n")
        for code, address in addresses.items():
            print(f"{code}. {address}")

        while True:
            address_choice = input("Please enter the code for your address:")
            if address_choice in addresses:
                selected_address = addresses[address_choice]
                print(f"You selected: {selected_address}/n")
                break
            else:
                print("Invalid address code selected. Please try again./n")

        # Write the selected address to the 'orders' sheet
        orders.append_row([new_code, selected_address])

    elif user_choice == '2':
        print("Checking order status...")
if __name__ == "__main__":
    main()

