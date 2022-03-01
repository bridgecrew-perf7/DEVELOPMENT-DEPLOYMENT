# Python Programming Best Practices

```python3
# import this

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

# examples

# This is bad
# represents the number of active users
au = 55

# This is good
active_user_amount = 55
We'll look at more examples in the next two sections.


# This is bad
c = 5
d = 12

# This is good
city_counter = 5
elapsed_time_in_days = 12


# This is bad
genyyyymmddhhmmss = datetime.strptime('04/27/95 07:14:22', '%m/%d/%y %H:%M:%S')

# This is good
generation_datetime = datetime.strptime('04/27/95 07:14:22', '%m/%d/%y %H:%M:%S')


# This is bad
fna = 'Bob'
cre_tmstp = 1621535852

# This is good
first_name = 'Bob'
creation_timestamp = 1621535852


# This is bad
client_first_name = 'Bob'
customer_last_name = 'Smith'

# This is good
client_first_name = 'Bob'
client_last_name = 'Smith'

# This is bad
def roll():
    return random.randint(0, 36)  # what is 36 supposed to represent?

# This is good
ROULETTE_POCKET_COUNT = 36

def roll():
    return random.randint(0, ROULETTE_POCKET_COUNT)


# This is good
score_list = [12, 33, 14, 24]
word_dict = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry',
}

# This is bad
names = ["Nick", "Mike", "John"]


# This is bad
class Person:
    def __init__(self, person_first_name, person_last_name, person_age):
        self.person_first_name = person_first_name
        self.person_last_name = person_last_name
        self.person_age = person_age


# This is good
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# This is bad
def get_name(): pass
def fetch_age(): pass

# This is good
def get_name(): pass
def get_age(): pass


# This is bad
def fetch_and_display_personnel():
    data = # ...

    for person in data:
        print(person)


# This is good
def fetch_personnel():
    return # ...

def display_personnel(data):
    for person in data:
        print(person)


# This is bad
def render_blog_post(title, author, created_timestamp, updated_timestamp, content):
    # ...

render_blog_post("Clean code", "Nik Tomazic", 1622148362, 1622148362, "...")


# This is good
class BlogPost:
    def __init__(self, title, author, created_timestamp, updated_timestamp, content):
        self.title = title
        self.author = author
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.content = content

blog_post1 = BlogPost("Clean code", "Nik Tomazic", 1622148362, 1622148362, "...")

def render_blog_post(blog_post):
    # ...

render_blog_post(blog_post1)

# This is bad
def transform(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()

uppercase_text = transform(text, True)
lowercase_text = transform(text, False)


# This is good
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

uppercase_text = uppercase(text)
lowercase_text = lowercase(text)
```
