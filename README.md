# Password-warehouse
## Author

~ Derick Ogendi
## Description

A python application that manages login and signup details of a use for various accounts i.e. username and passwords for each account. It also stores the passwords and auto-generates a unique password of 8 characters for a user if they do not want to type the passwords.


## User Stories
The user would like to do the following:
+ To create a password locker account with profile details, a login username and password.
+ To store user already existing account credentials in the application. Assuming the user already have a facebook account, user wants to store  already existing facebook username and password in this warehouse application.
+ Create new account credentials in the application. For example, if user has not signed up for Imo, user would want to create a credentials account for Imo in the application and the application generates a password for the user to use when they sign up for Imo.
+ Have the option of putting in a password that they want to use for the new credential account. For example, when creating  Imo credential account,user would want to have an option of putting in the password he/she want to use instead of having the application generate a password for them.
+ To view my various account credentials and their passwords in the application.
+ Delete a credentials account that user no longer need in the application.


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3
* pyperclip
* xclip
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ``https://github.com/OGENDI/passWarehouse.git``

 + or
 git clone ``git@github.com:OGENDI/passWarehouse.git``

* cd PasswordLocker

* Vs code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x launcher.py
        $ ./launcher.py
* To run test for the application

        $ python3 testing.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./launcher.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```UP``` to enter your password or ```SP``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```DEL```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|

## Technologies Used

* python3.8

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [ogendi18@gmail.com](ogendi18@gmail.com)

LinkedIn - [Derick Ogendi](https://www.linkedin.com/in/derick-ogendi/)


# Licence

Click to  [MIT License](Licence) view

 Copyright (c) 2022 | Derick Ogendi
