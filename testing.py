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

        

    