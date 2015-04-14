# melon_dictionaries = {
#      "melon_names": {
#         1: "Honeydew",
#         2: "Crenshaw",
#         3: "Crane",
#         4: "Casaba",
#         5: "Cantaloupe",
#     },
#
#     "melon_prices": {
#         1: 0.99,
#         2: 2.00,
#         3: 2.50,
#         4: 2.50,
#         5: 0.99,
#     },
#
#     "melon_seedlessness": {
#         1: True,
#         2: False,
#         3: False,
#         4: False,
#         5: False,
#     }
#     }

melon_dictionaries = {
    "cantelope": {
        "price": 0.99,
        "seeds": True   },
    "crenshaw": {
        "price": 2.00,
        "seeds": False   }
    }


def update_melon_dictionary(melon_dictionary, melon_number, melon_value):

    if melon_dictionary in melon_dictionaries:
        print "Adding %s: %s to existing dictionary %s" % (melon_number,
            melon_value, melon_dictionary)
        melon_dictionary = melon_dictionaries[melon_dictionary]
        melon_dictionary[melon_number] = melon_value

    else:
        print "Creating new dictionary %s and adding %s: %s" % (melon_dictionary,
            melon_number, melon_value)
        melon_dictionaries[melon_dictionary] = {}
        melon_dictionaries[melon_dictionary][melon_number] = melon_value

    print melon_dictionaries


update_melon_dictionary("cantelope", "color", "orange")
update_melon_dictionary("watermelon", "price", 0.99)
