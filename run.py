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
    
        addresses = get_address_options()
        print("Available addresses:")
        for code, address in addresses.items():
            print(f"{code}. {address}")

    elif user_choice == '2':
        print("Checking order status...")
        print(data)
if __name__ == "__main__":
    main()

