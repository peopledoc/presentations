import re

EMAIL_REGEXP = r'[\S.]+@[\S.]+'

def test_email_regexp():
   # a regular e-mail address should match
   assert re.match(EMAIL_REGEXP, 'test@nowhere.com')

   # no domain should fail
   assert not re.match(EMAIL_REGEXP, 'test@')
   
   # No extension should fail
   assert not re.match(EMAIL_REGEXP, 'test@nowhere')