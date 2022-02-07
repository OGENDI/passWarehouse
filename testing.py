import unittest
from user_details import User_account
from credentials import User_credentials

class Test_user_Account(unittest.TestCase):
    '''
    Class that defines test cases for the user account class behavious.
    '''
    def setUp(self):
        '''
        set up method to run before individual test cases
        '''
        self.new_user_account = User_account('Derick','Ogendi','Dogendi','CpFBaDYk')

    def tearDown(self):
        '''
        method that cleans up after each test case has run.
        '''
        User_account.user_accounts=[]

    def test_init(self):
        '''
        Test that checks object is initialized properly
        '''
        self.assertEqual(self.new_user_account.first_name,'Derick')
        self.assertEqual(self.new_user_account.last_name,'Ogendi')
        self.assertEqual(self.new_user_account.username,'Dogendi')
        self.assertEqual(self.new_user_account.password,'CpFBaDYk')

    def test_save_new_user(self):
        '''
        Tests if new user account has been save to list
        '''
        self.new_user_account.save_new_user()
        self.assertEqual(len(User_account.user_accounts),1)
    
    def test_save_multiple_accounts(self):
        '''
        Checks if user can save multiple accounts in the user account list
        '''
        self.new_user_account.save_new_user()
        Test_user_Account = User_account('TestUserFirstname','TestUserLastName','TestUsername','testPassword')
        Test_user_Account.save_new_user()
        self.assertEqual(len(User_account.user_accounts),2) 
    













       
if __name__ == '__main__':
    unittest.main()
        