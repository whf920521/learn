# !/usr/bin/python
import re

phone = "2001-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digite
num = re.sub(r'\D', "", phone)
print "Phone Num : ", num
