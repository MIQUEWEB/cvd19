from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



    def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('tablelist')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
                       raise e                  
                   time.sleep(0.5)  
                 
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_browser_title(self):
        self.browser.get('http://localhost:8000/')
     #self.browser.get(self.live_server_url)
        self.assertIn('COVID19 Vaccinated Record',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('COVID19 VACCINATED RECORD', header_text)
     
     
     #aaddress = self.browser.find_element_by_id('address')
    #aaddress.click()
    #time.sleep(1)
    #aadress.send_keys('blk 107 lot 8')
    #time.sleep(1)
    #pnumber = self.browser.find_element_by_id('number')
    #pnumber.click()
    
     inputname = self.browser.find_element_by_id('flname')
     self.assertEqual(inputname.get_attribute('placeholder'),'Enter first your Lastname, Firstname M.')
     inputname.click()
     time.sleep(1)
     inputname.send_keys('Ricca Mae Mique')
     
     time.sleep(1)
     
     
     inputaddress = self.browser.find_element_by_id('address')
     self.assertEqual(inputaddress.get_attribute('placeholder'),'PLease Enter your complete address')
     inputaddress.click()
     time.sleep(1)
     inputaddress.send_keys('Blk 107 lot 8 phase 8 ')
     time.sleep(1)
     
     
     inputphonenumber = self.browser.find_element_by_id('rnumber')
     self.assertEqual(inputphonenumber.get_attribute('placeholder'),'Enter your Number')
     inputphonenumber.click()
     time.sleep(1)
     inputphonenumber.send_keys('09457889')
     time.sleep(1)
     
    
     inputbirthday = self.browser.find_element_by_id('rmday')
     self.assertEqual(inputbirthday.get_attribute('placeholder'),'Date of Birth')
     inputbirthday.click()
     time.sleep(1)
     inputbirthday.send_keys('NOv 25')
     time.sleep(1)
     
     
     inputvaccine = self.browser.find_element_by_id('vaccine')
     self.assertEqual(inputvaccine.get_attribute('placeholder'),'VEnter Vaccine Product Name')
     inputvaccine.click()
     time.sleep(1)
     inputvaccine.send_keys('moderna')
     time.sleep(1)
     
     btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
     btnSubmit.click()
     time.sleep(2)
     


    
#rname.send_keys('Ricca Mae Mique')
    #time.sleep(1)
    #aaddress = self.browser.find_element_by_id('address')
    #aaddress.click()
    #time.sleep(1)
    #aadress.send_keys('blk 107 lot 8')
    #time.sleep(1)
    #pnumber = self.browser.find_element_by_id('number')
    #pnumber.click()
    #time.sleep(1)
    #pnumber.send_keys('Phone Number')
    #time.sleep(1)
    #eemail = self.browser.find_element_by_id('email')
    #number.click()
    #time.sleep(1)
    #eemail.send_keys('riccamae@gmail.com')
    #number.click()
    #time.sleep(1)
    #eemail.send_keys('riccamae@gmail.com')
    #time.sleep(1)
    #btnSub = self.browser.find_element_by_id('btnSubmit')
    #btnSub.click()
    #time.sleep(2)

    #elf.check_for_rows_in_list_table('1: Ricca Mae Mique blk 107 lot 8 phs 3 09355 ricac@gmail.com')
    #table =self.browser.find_element_by_id('listTable')
    #r#ows = table.find_element_by_tag_name('tr')

      
     #inputbox.click()
     
     #btnSubmit = self.browser.find_element_by_id('btnSubmit')
     #btnSubmit.click()


if __name__ == '__main__':
    unittest.main()