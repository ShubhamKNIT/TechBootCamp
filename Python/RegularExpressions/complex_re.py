import re

text = None
with open('data.txt', 'r') as f:
    text = f.read()

# # Matching phone number
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.finditer(text) 

# for match in matches:
#     print(match)
# #

# # # Matching email address
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+')
# matches = pattern.finditer(text) 

# for match in matches:
#     print(match)
# # #


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# # # Matching URLs
# pattern = re.compile(r'https?://(www\.)?(\w+\.)(\w+)')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match)
# # #

# # # Matching URLs and getting group (0 - full URL, 1 - www/None, 2 - domain, 3 - TLD)
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))
# # #

# # # Substituting text 
# pattern = re.compile(r'https?://(www\.)?(\w+\.)(\w+)')
# sub_urls = pattern.sub(r'\3', urls)

# print(sub_urls)
# # #

# # Case Insensitive Match and RegEx Flag
pattern = re.compile(r'COM', re.IGNORECASE)
matches = pattern.finditer(urls)

for match in matches:
    print(match)
# #