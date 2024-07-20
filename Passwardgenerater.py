import random

#Random password generating

uppercase_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter=uppercase_letter.lower()
numerics="0123456789"
symbols= "(){|}[]~!@#$%^&*_-`:;/.,?><'"

all_character =''+uppercase_letter+lowercase_letter+numerics+symbols

Passwordlength=int(input("Enter the length of the password:"))

password="".join(random.sample(all_character,Passwordlength))
print("Password is:",password)