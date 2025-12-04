print("This is the Password Generator project")
import random
import string
def generate_password(length=12):

    list1 = string.ascii_lowercase
    list2 = string.ascii_uppercase
    list3 = string.digits
    list4 = string.punctuation
    combined_list = list1 + list2 + list3 + list4
    password = ''.join(random.sample(combined_list, length))
    return password

print("Your Generated Password:", generate_password(12))
