import random
import string
from pages.base_page import BasePage


# def randomtext(complexity, length):
#     if complexity == 'weak':
#         return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
#
#     if complexity == 'medium':
#         return ''.join(random.choice(string.ascii_letters) for i in range(length))
#
#     if complexity == 'strong':
#         return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
#
#     if complexity == 'super_strong':
#         return ''.join(random.choice(string.printable) for i in range(length))
#
#     if complexity == 'special':
#         return ''.join(random.choice(string.punctuation) for i in range(length))
#
#
# print(randomtext('medium', 10) + '@gmail.com')
# text = randomtext('weak', 10) + '@email.com'
# print(text)
