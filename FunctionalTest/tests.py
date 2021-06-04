from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10
class PageTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()

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
                 
    

    def test_browser_title(self):
        self.browser.get('http://localhost:8000')
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
    
        inputmunicipality = self.browser.find_element_by_id('flmunicipality')
        self.assertEqual(inputmunicipality.get_attribute('placeholder'),'Your Municipality')
        inputmunicipality.click()
        time.sleep(1)
        inputmunicipality.send_keys('Dasma')
        time.sleep(1)
     
     
        inputbaranggay = self.browser.find_element_by_id('zzbaranggay')
        self.assertEqual(inputbaranggay.get_attribute('placeholder'),'Enter your Baranggay')
        inputbaranggay.click()
        time.sleep(1)
        inputbaranggay.send_keys('Paliparan III ')
        time.sleep(1)
        btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
        btnSubmit.click()
        time.sleep(2)
    
     
     
        inputname = self.browser.find_element_by_id('zvname')
        self.assertEqual(inputname.get_attribute('placeholder'),'First Name MI Lastname')
        inputname.click()
        time.sleep(1)
        inputname.send_keys('Ricca')
        time.sleep(1)
       
        inputaddress = self.browser.find_element_by_id('xxaddress')
        self.assertEqual(inputaddress.get_attribute('placeholder'),'Your Address')
        inputaddress.click()
        time.sleep(1)
        inputaddress.send_keys('Blk 107 LOt 8 phase 3')
        time.sleep(1)
        
        inputgender = self.browser.find_element_by_id('rjgender')
        self.assertEqual(inputgender.get_attribute('placeholder'),'Your Gender')
        inputgender.click()
        time.sleep(1)
        inputgender.send_keys('female')
        time.sleep(1)
        inputnumber = self.browser.find_element_by_id('contactn')
        self.assertEqual(inputnumber.get_attribute('placeholder'),'Your Contact Number')
        inputnumber.click()
        time.sleep(1)
        inputnumber.send_keys('09457996708')
        time.sleep(1)
        inputphilnum = self.browser.find_element_by_id('philnumber')
        self.assertEqual(inputphilnum.get_attribute('placeholder'),'Your Phil Health Number')
        inputphilnum.click()
        time.sleep(1)
        inputphilnum.send_keys('252525')
        time.sleep(1)
        inputbirthday = self.browser.find_element_by_id('kkbirthday')
        self.assertEqual(inputbirthday.get_attribute('placeholder'),'Your Birthday')
        inputbirthday.click()
        time.sleep(1)
        inputbirthday.send_keys('1999-11-25')
        time.sleep(1)
        btnSubmit = self.browser.find_element_by_id('submitrr')
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
