import phonenumbers

'''geocoder: to know the specific
location to that phone number
carrier: to know the name of
service provider of that phone number'''

from phonenumbers import carrier
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+918*********")

# this will print the service provider name
print(carrier.name_for_number(phone_number,
                              'en'))

# this will print the country name
print(geocoder.description_for_number(phone_number,
                                      'en'))
