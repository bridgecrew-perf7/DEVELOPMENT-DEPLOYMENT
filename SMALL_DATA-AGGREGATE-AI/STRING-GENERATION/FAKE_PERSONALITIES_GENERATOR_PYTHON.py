from faker import Faker
import random
import string
import time
import schedule

fake = Faker('de_DE')

def birthday_cleaner(birthday):
    birthday = birthday.split("-")
    return birthday

def replace_umlaute(s):
    umlaute = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue','ß': 'ss', 'é': 'e', '\'': '', ' ': ''}
    s = s.lower()
    for u in umlaute:
        s = s.replace(u, umlaute[u])
    return s

def generate_email_prefix(first_name: str, last_name: str, birthday: str):

    splitter = ("yo", "top", "-", "_", "", "er", "ko", "si", "bi", "ger")
    firstname_combs = (first_name, first_name)
    lastname_combs = (last_name, last_name)
    birthdate_splitted = birthday.split('-')

    birthdate_combs = (birthdate_splitted[2], birthdate_splitted[1], birthdate_splitted[0])
    combinations = {0: f"{random.choice(lastname_combs)}{random.choice(splitter)}{random.choice(birthdate_combs)}",
                    1: f"{random.choice(firstname_combs)}{random.choice(splitter)}{random.choice(birthdate_combs)}"}

    email_ranom_digits = ''.join(random.choice(string.digits) for i in range(3))
    email_prefix = random.choice(combinations).lower() + email_ranom_digits
    email = replace_umlaute(email_prefix)
    return email


def generate_password(special_char_factor=2):
    chars_fixed = string.ascii_letters + string.digits + '$#*-_.:(){}/&!?' * \
        special_char_factor
    password = "".join(random.choice(chars_fixed)
                       for x in range(random.randint(4, 9)))
    password = fake.last_name() + password
    return password

# time slot check
# if NOT timeslot
# if db >1200

# push 6000 entry csv to db sqlite

# wait 1m
# schedule

first_name = fake.first_name()
first_name.append
last_name = fake.last_name()
addr = fake.address()
birthday = str(fake.date_between(start_date='-70y', end_date='-20y'))
ua = fake.user_agent()

def fake_invoker(entity, range):
    for _ in range(range):
        return fake.entity
