############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType("musk", "1998", "green", True, True, "muskmelon")
    casaba = MelonType("cas", "2003", "orange", False, False, "casaba")
    crenshaw = MelonType("cren", "1996", "green", False, False, "crenshaw")
    yellow_watermelon = MelonType("yw", "2013", "yellow", False, True, "Yellow Watermelon")

    muskmelon.add_pairing('mint')
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("proscuitto")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)


    # print(casaba.pairings)

    return all_melon_types

# melon_type = make_melon_types()
# print_pairing_info(melon_type)


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for index in range(len(melon.pairings)):
            print(f"-{melon.pairings[index]}")
   
    # print(type(melon.pairings))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_codes = {}

    for melon in melon_types:
        melon_codes[melon.code] = melon

    return melon_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, harvest_from_field, harvest_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_from_field = harvest_from_field
        self.harvest_by = harvest_by

    def is_sellable(self, shape_rating, color_rating, harvest_from_field):

        if shape_rating > 5 and color_rating > 5 and harvest_from_field != 3:
            return True
        
        return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_codes_dict = make_melon_type_lookup(melon_types)
    # Fill in the rest
    # access the value in the dictionary for each item in the melon_type list
    # compare if the new melons are in the dictionary
    # if not, then add the new melons to the melon type list
    

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 




melon_list = make_melon_types()
# print(melon_list)
print_pairing_info(melon_list)

# melon = MelonType("a", "b", "c", "d", "e", "f")
# pair = melon.pairings

codes_melon = make_melon_type_lookup(melon_list)
print(codes_melon)
print(codes_melon["cas"].color) 
