from pprint import pprint

# admin_login = 'admin'
# admin_password = '123'
# admin_salary = 5222
# admin_hobbies = ['tennis', 'soccer']
# is_married = True

# CREATE
admin_data = {
    "login": 'pavel',
    "password": '123',
    "salary": 2500,
    "hobbies": [
        'теніс',
        'soccer'
    ],
    'is_married': True,
    "address": {
        'city': 'Lviv',
        'street': "Soborna",
        'building': 15,
        # 'apartment': 56
    },
    'pet_name': None,
}

# print(admin_data)
# pprint(admin_data)

# READ
admin_login = admin_data["login"]
print(admin_login)
admin_city = admin_data["address"]['city']
print(admin_city)

# apartment = admin_data["address"]['apartment']
# print(apartment)

admin_address = admin_data["address"]
print(admin_address)
# apartment = admin_address.get('apartment')
apartment = admin_address.get('apartment', 'N/A')
print(apartment)

salary_grn = admin_data["salary"] * 44
print(salary_grn)

hobbies = admin_data['hobbies']
print(hobbies)

if hobbies:
    print(hobbies[0])

# UPDATE

# add data
admin_data['birthday'] = '11.11.1990'


# change data
admin_data['pet_name'] = 'Barsik'

admin_data['hobbies'].append('swimming')

admin_data["address"]['country'] = 'Ukraine'
# pprint(admin_data)

admin_extra_data = {
    "car": 'TOYOTA',
    'pet': "dog",
    "salary": 6000,
}

# rate = 49.0
# rate = round(rate, -2)
# print(rate)
#
# 100/rate

# update existing
# admin_data.update(admin_extra_data)
# pprint(admin_data)

# create new dict merged
# full_admin_cv = admin_data | admin_extra_data
full_admin_cv = {**admin_data, **admin_extra_data}
# pprint(admin_data)
pprint(full_admin_cv)

# DELETE
# del full_admin_cv['birthday']
birthday = full_admin_cv.pop('birthday')
print(birthday)
pprint(full_admin_cv)