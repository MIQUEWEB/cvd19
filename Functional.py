from selenium import webdriver
import unittest

class Test(unittest.TestCase):  #1

    
 def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

 def tearDown(self):

    
        # homepage
        self.browser.get('http://localhost:8000')

        
        self.assertIn('To-Do', self.browser.title)  #5
        self.fail('Finish the test!')  #6

        
   

if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #
