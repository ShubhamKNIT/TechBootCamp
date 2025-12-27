import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end' 

# # #
# print('\t', sentence) # formatted tabline sentence
# print(r'\tTab') # raw string - without formatting
# # #

# # # Simple Pattern
# pattern = re.compile(r'abc') # create a pattern using re.compile(<raw_string>)
# matches = pattern.finditer(text_to_search) # <re.compile Object>.finditer(<multiline_string>)

# # finditer() finds all the pattern match (case-sensitive)
# for match in matches: <matches : regex match iterator>
#     print(match)
# # #

# # # Matching Characters requiring escape character
# pattern = re.compile(r'coreyms\.com')
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)
# # #

# # # Matching boundary/non-boundary words
# pattern = re.compile(r'\BHa')
# matches = pattern.finditer(text_to_search) 

# for match in matches:
#     print(match)
# # #