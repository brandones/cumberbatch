""" cumberbatch.py

    Returns random English names using the content of lists.py.
"""

import random


def first(clean=True):
    """ A randomized English first name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    if clean:
        return random.choice(Lists.firstnames)
    else:
        return random.choice(Lists.firstnames + Lists.firstnames_unclean)


def last(clean=True):
    """ A randomized English last name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    if clean:
        return random.choice(Lists.lastnames)
    else:
        return random.choice(Lists.lastnames + Lists.lastnames_unclean)


def full(clean=True):
    """ A randomized full English name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    # Roll to see if we should just pick a full name
    # This probability is equal to the probability of any other full
    # name being composed.

    if clean:
        num_name_combos = len(Lists.firstnames) * len(Lists.lastnames)
        num_full_names = len(Lists.fullnames)
    else:
        num_name_combos = ((len(Lists.firstnames) + len(Lists.firstnames_unclean)) *
                           (len(Lists.lastnames_unclean) + len(Lists.lastnames_unclean)))
        num_full_names = len(Lists.fullnames) + len(Lists.fullnames_unclean)

    p_arbitrary_pair = 1 / num_name_combos
    p_full_name = p_arbitrary_pair * num_full_names
    if random.random() < p_full_name:
        if clean:
            return random.choice(Lists.fullnames)
        else:
            return random.choice(Lists.fullnames + Lists.fullnames_unclean)

    # We didn't select a full name, so let's compose a random name
    if clean:
        firstname = random.choice(Lists.firstnames)
        lastname = random.choice(Lists.lastnames)
    else:
        firstname = random.choice(Lists.firstnames + Lists.firstnames_unclean)
        lastname = random.choice(Lists.lastnames + Lists.lastnames_unclean)

    return '{} {}'.format(firstname, lastname)


class Lists(object):
    """ Most content mercilessly and unrepentantly pirated from
        http://benedictcumberbatchgenerator.tumblr.com/
    """

    firstnames = (
        "Anglerfish",
        "Bakery",
        "Bandersnatch",
        "Bandicoot",
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
        "Benetton",
        "Benjamin",
        "Bentobox",
        "Bentobox",
        "Billiardball",
        "Billyray",
        "Blasphemy",
        "Blubberwhale",
        "Bodybuild",
        "Boilerdang",
        "Bombadil",
        "Bombadil",
        "Bonaparte",
        "Boobytrap",
        "Bouillabaisse",
        "Bourgeoisie",
        "Brandenburg",
        "Brandybuck",
        "Brewery",
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
        "Bunsenburner",
        "Burberry",
        "Burgerking",
        "Burlington",
        "Buttercup",
        "Butterfree",
        "Buttermilk",
        "Cogglesnatch",
        "Congleton",
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
        "Syphilis"
    )

    lastnames = (
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
        "Coggleswort",
        "Collywog",
        "Colonist",
        "Commonwealth",
        "Combaba",
        "Concubine",
        "Copperwire",
        "Cottagecheese",
        "Countryside",
        "Covergirl",
        "Crackerjack",
        "Crackersprout",
        "Cragglethatch",
        "Creamsicle",
        "Crimpysnitch",
        "Crucifix",
        "Crumplebutt",
        "Crumplehorn",
        "Crumplesack",
        "Cuckatoo",
        "Cuckooclock",
        "Cumberbund",
        "Cumbersnatch",
        "Cumbersome",
        "Cummerbund",
        "Cunningsnatch",
        "Curdledmilk",
        "Curdlemilk",
        "Curdlesnoot",
        "Custardbath",
        "Cuttlefish",
        "Frumblesnatch",
        "Humperdinck",
        "Kryptonite",
        "Lingerie",
        "Moldyspore",
        "Nottinghill",
        "Oxfordshire",
        "Rivendell",
        "Scratchnsniff",
        "Snickersbar",
        "Snugglesnatch",
        "Splishnsplash",
        "Stinkyrash",
        "Talisman",
        "Toodlesnoot",
        "Upperclass",
        "Vegemite",
        "Wafflesmack"
    )

    lastnames_unclean = (
        "Cameltoe",
        "Cockletit",
        "Coochierash",
        "Crackerdong",
        "Cumbercooch",
        "Cuntersnatch",
        "Curdledong"
    )

    fullnames = (
        "Benadryl Claritin",
        "Benedict Timothy Carlton Cumberbatch",
        "Biblical Concubine",
        "Bombadil Rivendell",
        "Bourgeoisie Capitas",
        "Buckminster Fullerene",
        "Butawhiteboy Cantbekhan",
        "Rinkydink Curdlesnoot",
        "Wanda's Son",
        "Wimbledon Tennismatch"
    )

    fullnames_unclean = (
        "Syphilis Cankersore",
        "Wanda's Crotchfruit"
    )
