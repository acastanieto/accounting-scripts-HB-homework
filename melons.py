melon_dictionaries = {
    "melon_names": {
        1: "Honeydew",
        2: "Crenshaw",
        3: "Crane",
        4: "Casaba",
        5: "Cantaloupe",
    },

    "melon_prices": {
        1: 0.99,
        2: 2.00,
        3: 2.50,
        4: 2.50,
        5: 0.99,
    },

    "melon_seedlessness": {
        1: True,
        2: False,
        3: False,
        4: False,
        5: False,
    }
}

def add_to_melon_dictionary(melon_dictionary, melon_number, melon_value):
    if melon_dictionary in melon_dictionaries:
        melon_dictionaries[melon_dictionary[melon_number]] = melon_value
    else:
        melon_dictionaries[melon_dictionary] = {}
        melon_dictionaries[melon_dictionary[melon_number]] = melon_value
    print melon_dictionaries   

add_to_melon_dictionary("melon_names", 6, "Watermelon")
add_to_melon_dictionary("melon_color", 1, "green")
