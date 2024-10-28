import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+63 Your Phone Number")
phone_number2 = phonenumbers.parse("+63 Your Phone Number") 

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
