import re

prog = re.compile(r'\w\w')

searched_item_1 = re.search(r'\w\w', 'Hello World Using Regex')
searched_item_2 = re.findall(r'\w\w\b', 'Hello World Using Regex')
print(searched_item_1)
print(searched_item_2)