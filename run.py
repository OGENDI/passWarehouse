from random import choice
from user_details import User_account
from credentials import User_credentials

def create_newuser_account(first_name,last_name,username,password):
    new_user_account = User_account(first_name,last_name,username,password)
    return new_user_account

def save_user_account(user_account):
    user_account.save_new_user()

def display_user_account():
    return User_account.display_users()
    
def user_login(username,password):
    verified_user_account = User_credentials.user_verification(username,password)
    return verified_user_account

# User credentials actions

def create_newuser_credential(my_account_name,username,password):
    new_user_credential = User_credentials(my_account_name,username,password)
    return new_user_credential

def save_user_credential(user_credential):
    user_credential.save_credentials()

def delete_credential(credentials):
    credentials.delete_user_credential()

def display_user_credentials():
    return User_credentials.display_user_credentials()

def find_user_credentials(user_account):
    return User_credentials.find_user_credential(user_account)

def do_credentials_exist(account):
    return User_credentials.do_credentials_exist(account)

def copy_password(user_account):
    return User_credentials.copy_login_password(user_account)

def system_generated_password():
    auto_generated_random_password = User_credentials.gen_random_password()
    return auto_generated_random_password

#****************************************************************************#


def my_password_master():
    print('--------------------Welcome to your password vault-----------------------')
    print('Please enter your name before we proceed. ')

    visitor = input()

    print(f'Hello {visitor}. Key in any of the following commands ')
    print('LI -------> To login in existing account')
    print('CA -------> To create a new user account')

    commands = input('').upper().strip()

    if commands == 'CA':
        print('<------Sign Up------->')
        first_name = input('Type your first name: ')
        last_name = input('Type your last name: ')
        username = input('Type your preferred username: ')
        while True:
            print('     SP -----> System Generated Password')
            print('     UP -------> User defined Password')

            user_entry = input('').upper()
            if user_entry == 'SP':
                password = system_generated_password()
                break
            elif user_entry == 'UP':
                password = input('Please type your preferred password: ')
                break
            else:
                print('Invalid choice, try again!')
        save_user_account(create_newuser_account(first_name,last_name,username,password))
        print(f'Thank you {visitor}. You have successfully signed up.')
        display_user_account()

    elif commands == 'LI':
        print('Enter your details to log in: ')
        username = input('Username: ')
        password = input('Password: ')
        user_logins = user_login(password)
        if user_login == user_logins:
            print(f'Hello, {username}. Welcome to your Password Vault.')

    while True:
        print('Use any of the following short codes to proceed: ')
        print('CC ----> Create new user credential ')
        print('DC ----> Display existing account credentils')
        print('FC ----> Find user credentials')
        print('GP ----> System generated password')
        print('DEL ---> Delete account credentials')
        print('EX ----> Exit the application')

        user_input = input('').upper().strip()

        if user_input == 'CC':
            print('Create user account credentials')
            print('Enter account name: ')
            user_account_name = input().strip()  

            print('Username for above account')
            
            account_username = input().strip()
            while True:
                print('A ---> Type existing password: ')
                print('B ---> System generated password: ')
                
                choice = input().strip()

                if choice == 'A':
                    password = input('Type Password: ')
                    break
                elif choice == 'B':
                    password = system_generated_password()
                    break
                else:
                    print('Invalid choice. Type again')
            save_user_credential(create_newuser_credential(user_account_name,account_username,password))
            print('')
            print(f'Credential details for {user_account_name} Username {account_username} and Password {password}')

        elif user_input == 'DC':
            if display_user_credentials():
                print('Check a list of available accounts in the vault: ')
                print('')
                for profile in display_user_credentials():
                    print(f'Profile: {profile.my_account}')
                    print(f'Username: {username}')
                    print(f'Password: {password}')
                    print('')
            
            else:
                print('There are no credentials saved')
        elif user_input == 'FC':
            print('Enter account to search: ')
            account_name = input().strip()
            if find_user_credentials(account_name):
                search_account = find_user_credentials(account_name)
                print(f'Account: {search_account.my_account} ')
                print(f'Username: {search_account.username}')
            else:
                print(f'The account name does not exist.')
        elif user_input == 'GP':
            password = system_generated_password()
            print(f'The system generated password is: {password}')
        elif user_input == 'DEL':
            print('Enter account to delete: ')
            account_name = input().strip()
            if find_user_credentials(account_name):
                search_account = find_user_credentials(account_name)
                print('')
                search_account.delete_user_credential()
                print(f'{search_account.my_account} deleted.')
            else:
                print(f'{account_name} Account does not exist.')
        elif user_input == 'EX':
            print('Thank you. See you again!')
            break
        else:
            print('Invalid entry. Try again')

if __name__ == '__main__':
    my_password_master()


