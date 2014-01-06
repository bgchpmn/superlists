from django.test import LiveServerTestCase
from selenium import webdriver
import sys

class FunctionalTest(LiveServerTestCase):
        
    @classmethod
    def setUpClass(cls):
        """docstring for setUpClass"""
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        LiveServerTestCase.setUpClass()
        cls.server_url = cls.live_server_url
    
    @classmethod
    def tearDownClass(cls):
        """docstring for tearDownClass"""
        if cls.server_url == cls.live_server_url:
            LiveServerTestCase.tearDownClass()
    
    def setUp(self):
        """docstring for setUp"""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        """docstring for tearDown"""
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        """helper method for later tests"""
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])