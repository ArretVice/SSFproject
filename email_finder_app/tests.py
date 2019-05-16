from django.test import TestCase
from .customfunctions import get_list_of_emails


# Create your tests here.
class EmailFinderTestCase(TestCase):
    def test_get_list_of_emails(self):
        test_string = '''
        Hello mister Anderson, is your e-mail adress MisterAnderson@matrix.com?
        We would expect you to have something like Neo.is.a-cool_hackst3r@bullshit.ua, or maybe some +- actions?
        Anything about 95823ufmlkwe@fda.balls seems familiar to you@. No?
        '''
        self.assertEqual(get_list_of_emails(test_string), ['MisterAnderson@matrix.com', 'Neo.is.a-cool_hackst3r@bullshit.ua', '95823ufmlkwe@fda.balls'])
        self.assertEqual(get_list_of_emails('String with no emails in it'), [])
        self.assertEqual(get_list_of_emails('abra_cada+bra.@sample-mailservice.boring'), ['abra_cada+bra.@sample-mailservice.boring'])