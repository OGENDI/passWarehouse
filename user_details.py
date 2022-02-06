class User_account:
    '''
    Account for user where they create their profiles and store the details
    '''
    user_accounts = []

    def __init__(self, first_name, last_name, username, password):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_new_user(self):
        '''
        method used to save new users to user_accounts list
        '''
        User_account.user_accounts.append(self)

    def delete_user_account():
        '''
        method used to delete existing users from the list
        '''
        User_account.user_accounts.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method used to display a user from the list
        '''
        return cls.user_accounts
    