""" __init__.py.py

    Returns random English names similar to Benedict Cumberbatch.
"""

import random

def first(clean=True):
    """ A randomized English first name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    return random.choice(Lists.firstnames[clean])


def last(clean=True):
    """ A randomized English last name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    return random.choice(Lists.lastnames[clean])


def full(clean=True):
    """ A randomized full English name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    # Roll to see if we should just pick a full name
    if __pick_fullname_from_list(clean):
        return random.choice(Lists.fullnames[clean])

    # We didn't select a full name, so let's compose a random name
    return __compose_name(clean)


__p_full_name = {}  # a dict indexed by the boolean 'clean'
def __pick_fullname_from_list(clean):
    """ Flip a coin to choose between fullnames list and composing one

    The probability of choosing a fullname is equal to the probability
    of any other full name being composed.

    Stores the calculated probability in __p_full_name_*

    :param clean: Whether to use the lengths of the _clean or _all lists
    :return: boolean
    """
    if clean not in __p_full_name:
        num_name_combos = len(Lists.firstnames[clean]) * len(Lists.lastnames[clean])
        num_full_names = len(Lists.fullnames[clean])
        p_arbitrary_pair = 1 / num_name_combos
        __p_full_name[clean] = p_arbitrary_pair * num_full_names
    return random.random() < __p_full_name[clean]


def __compose_name(clean):
    """
    :param clean: Whether to use the lengths of the _clean or _all lists
    :return: str -- a full name.
    """
    firstname = random.choice(Lists.firstnames[clean])
    lastname = random.choice(Lists.lastnames[clean])

    # If the name has neither a first name starting with a B nor a
    # last name starting with a C, re-roll.
    if not firstname.startswith('B') and not lastname.startswith('C'):
        return __compose_name(clean)
    else:
        return '{} {}'.format(firstname, lastname)


class Lists(object):
    """ Most content mercilessly and unrepentantly pirated from
        http://benedictcumberbatchgenerator.tumblr.com/
    """

    firstnames_clean = (
        "Anglerfish",
        "Bakery",
        "Balderdash",
        "Bandersnatch",
        "Bandicoot",
        "Bandingo",
        "Bandydoo",
        "Barister",
        "Barnoldswick",
        "Baseballbat",
        "Baseballmitt",
        "Bedlington",
        "Beetlejuice",
        "Beezlebub",
        "Benadryl",
        "Bendandsnap",
        "Bendyguy",
        "Benetton",
        "Benjamin",
        "Bentobox",
        "Billiardball",
        "Billyray",
        "Blasphemy",
        "Blubberwhale",
        "Bodybuild",
        "Boilerdang",
        "Bombadil",
        "Bonaparte",
        "Bonnydoon",
        "Boobytrap",
        "Bouillabaisse",
        "Bourgeoisie",
        "Brandenburg",
        "Brandybuck",
        "Brewery",
        "Briarpatch",
        "Broccoli",
        "Buckingham",
        "Buckminster",
        "Buckyball",
        "Budapest",
        "Buffalo",
        "Bulbasaur",
        "Bumberstump",
        "Bumblebee",
        "Bumbleshack",
        "Bumblesnort",
        "Bunsenburner",
        "Burberry",
        "Burgerking",
        "Burlington",
        "Buttercup",
        "Butterfree",
        "Buttermilk",
        "Cogglesnatch",
        "Congleton",
        "Shenanigans",
        "Danglerack",
        "Fragglerock",
        "Honkytonk",
        "Johnnycash",
        "Liverswort",
        "Muffintop",
        "Oscarbait",
        "Pallettown",
        "Rinkydink",
        "Rumblesack",
        "Snorkeldink",
        "Snozzlebert",
        "Tiddleywomp",
        "Timothy",
        "Wellington",
        "Whippersnatch",
        "Wimbledon"
    )

    firstnames_unclean = (
        "Anallube",
        "Barbituate",
        "Bendydick",
        "Blenderdick",
        "Blubberbutt",
        "Blubberdick",
        "Bukkake",
        "Bumblefuck",
        "Syphilis"
    )

    lastnames_clean = (
        "Ampersand",
        "Animorph",
        "Banglesnatch",
        "Battleship",
        "Bumbersplat",
        "Cabbagepatch",
        "Calldispatch",
        "Camouflage",
        "Candlestick",
        "Candycrush",
        "Candygram",
        "Cankersore",
        "Capncrunch",
        "Carrotstick",
        "Charizard",
        "Cheddarcheese",
        "Chesterfield",
        "Chickenbroth",
        "Chickenstrips",
        "Chowderpants",
        "Chuckecheese",
        "Clavichord",
        "Clombyclomp",
        "Coddleswort",
        "Coelacanth",
        "Coggleswort",
        "Collywog",
        "Colonist",
        "Combaba",
        "Commonwealth",
        "Copperwire",
        "Cottagecheese",
        "Countryside",
        "Crackerjack",
        "Crackersprout",
        "Cragglethatch",
        "Creamsicle",
        "Crimpysnitch",
        "Crucifix",
        "Crumplehorn",
        "Crumplesack",
        "Cuckatoo",
        "Cuckooclock",
        "Cumberbund",
        "Cumbersnatch",
        "Cumbersome",
        "Cummerbund",
        "Curdledmilk",
        "Curdlemilk",
        "Curdlesnoot",
        "Custardbath",
        "Cuttherug",
        "Cuttlefish",
        "Fettywap",
        "Frumblesnatch",
        "Humperdinck",
        "Kafkabadge",
        "Kafkablast",
        "Kryptonite",
        "Moldyspore",
        "Nottinghill",
        "Oxfordshire",
        "Rivendell",
        "Scratchnsniff",
        "Snickersbar",
        "Snugglesnatch",
        "Splishnsplash",
        "Talisman",
        "Toodlesnoot",
        "Upperclass",
        "Vegemite",
        "Wafflesmack"
    )

    lastnames_unclean = (
        "Cameltoe",
        "Cockletit",
        "Concubine",
        "Coochierash",
        "Covergirl",
        "Crackerdong",
        "Crumplebutt",
        "Cumberbitch",
        "Cumbercooch",
        "Cunnilingus",
        "Cunningsnatch",
        "Cuntersnatch",
        "Curdledong",
        "Lingerie",
        "Stinkyrash"
    )

    fullnames_clean = (
        "Benadryl Claritin",
        "Bombadil Rivendell",
        "Bourgeoisie Capitas",
        "Buckminster Fullerene",
        "Butawhiteboy Cantbekhan",
        "Eggsbenedict Breakfastbatch",
        "Frumtuous Bandersnatch",
        "Rinkydink Curdlesnoot",
        "Wanda's Son",
        "Wimbledon Tennismatch"
    )

    fullnames_unclean = (
        "Biblical Concubine",
        "Dandypants Frumplecooch",
        "Syphilis Cankersore",
        "Wanda's Crotchfruit"
    )

    firstnames_all = firstnames_clean + firstnames_unclean
    lastnames_all = lastnames_clean + lastnames_unclean
    fullnames_all = fullnames_clean + fullnames_unclean

    # Store these things in a dict indexed by the boolean variable 'clean'
    firstnames = {
        True: firstnames_clean,
        False: firstnames_all
    }

    lastnames = {
        True: lastnames_clean,
        False: lastnames_all
    }

    fullnames = {
        True: fullnames_clean,
        False: fullnames_all
    }
