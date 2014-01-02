from django.test import TestCase

class SmokeTest(TestCase):
    
    def test_bad_maths(self):
        """docstring for test_bad_maths"""
        self.assertEqual(1+1, 3)