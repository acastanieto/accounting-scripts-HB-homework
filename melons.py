from melonsdicts import melon_dictionaries

def update_melon_dictionary(melon_dictionary, melon_key, melon_value):

    if melon_dictionary in melon_dictionaries:
        print "Adding %s: %s to existing dictionary %s" % (melon_key,
            melon_value, melon_dictionary)
        melon_dictionary = melon_dictionaries[melon_dictionary]
        melon_dictionary[melon_key] = melon_value

    else:
        print "Creating new dictionary %s and adding %s: %s" % (melon_dictionary,
            melon_key, melon_value)
        melon_dictionaries[melon_dictionary] = {}
        melon_dictionaries[melon_dictionary][melon_key] = melon_value

    return melon_dictionaries

def print_melon_info(melon_dictionaries):
    print "Updated melon information:"
    for melon, info_dict in melon_dictionaries.items():
        print "Melon type: %s" % melon
        for info, values in info_dict.items():
            print info, values
        print "\n"

print_melon_info(update_melon_dictionary("Cantaloupe", "color", "orange"))
print_melon_info(update_melon_dictionary("Watermelon", "price", 0.99))
