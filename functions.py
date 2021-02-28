"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here
def hometown(name):
    """function to test whether name of hometown is san francisco"""
    if name.lower == "san francisco":
        return True
    else:
        return False
print(hometown("oakland"))

"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here
def full_name(first_name, last_name):
    """function that combines first and last name"""
    fullname = first_name + " " + last_name
    return fullname

print(full_name("Brighticorn", "Hackbright"))


"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

# Write your function here

def hometown_greeting(first_name, last_name, home_town):
    "function that checks if a person is from the same hometown prints a greeting"

    if home_town.lower() == "san francisco":
       return(f"Hi {first_name} {last_name}, we're from the same place!")
    else:
        return(f"Hi {first_name} {last_name}, I'd like to visit {home_town}!")


print(hometown_greeting('Mel', 'M', 'San Francisco'))
print(hometown_greeting('Fido', 'Bark', 'Oakland'))



"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# Write your function here

def is_berry(fruit):
    """function to check if fruit is a berry"""
    berry_types = ["currant", "goji"]
    if fruit[-5:] == "berry" or fruit in berry_types:
        return True
    else:
        return False

print(is_berry("strawberry"))
print(is_berry("currant"))

"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here
def shipping_cost(item):
    """function to determine cost of shipping an item"""
    berry_types = ["currant", "goji"]
    if item[-5:] == "berry" or item in berry_types:
        cost= 0
    else:
        cost=5
    return cost

print(shipping_cost("paper"))

"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here
def price_after_tax(base_price, state, tax=0.05):
    """function to calculate item cost after adding taxes and fees"""

    if state.lower() == "ca":
        tax = 0.03
        base_price += (tax*base_price)
        return base_price
    
    elif state.lower() == "pa":
        tax = 2
        base_price += tax
        return base_price

    elif state.lower() == "ma":
        if base_price <= 100:
            tax = 1
            base_price += tax
        if base_price > 100:
            tax = 3
            base_price += tax
            return base_price
        else: 
            return state

print(price_after_tax(5, "CA", 0.03))
print(price_after_tax(5, "PA"))



"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here

def add_to_list(list, *args):
    """function that adds any number of arguments to a list"""
    list.extend(args)
    return list
print(add_to_list([1, 2, 3], 4, 5, 6))


"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here

def word_to_tuple(word):
    """function that converts a word into a tuple"""
    convert = (word, word*3)
    return convert

print(word_to_tuple("hello"))
