""" benedict.py

    Returns random English names using the content of lists.py.
"""

import lists
import random


def first(clean=True):
    """ A randomized English first name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    if clean:
        return random.choice(lists.firstnames)
    else:
        return random.choice(lists.firstnames + lists.firstnames_unclean)


def last(clean=True):
    """ A randomized English last name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    if clean:
        return random.choice(lists.lastnames)
    else:
        return random.choice(lists.lastnames + lists.lastnames_unclean)


def full(clean=True):
    """ A randomized full English name.
    :param clean: If false, returns some names your boss may find objectionable
    """
    # Roll to see if we should just pick a full name
    # This probability is equal to the probability of any other full
    # name being composed.

    if clean:
        num_name_combos = len(lists.firstnames) * len(lists.lastnames)
        num_full_names = len(lists.fullnames)
    else:
        num_name_combos = ((len(lists.firstnames) + len(lists.firstnames_unclean)) *
                           (len(lists.lastnames_unclean) + len(lists.lastnames_unclean)))
        num_full_names = len(lists.fullnames) + len(lists.fullnames_unclean)

    p_arbitrary_pair = 1 / num_name_combos
    p_full_name = p_arbitrary_pair * num_full_names
    if random.random() < p_full_name:
        if clean:
            return random.choice(lists.fullnames)
        else:
            return random.choice(lists.fullnames + lists.fullnames_unclean)

    # We didn't select a full name, so let's compose a random name
    if clean:
        firstname = random.choice(lists.firstnames)
        lastname = random.choice(lists.lastnames)
    else:
        firstname = random.choice(lists.firstnames + lists.firstnames_unclean)
        lastname = random.choice(lists.lastnames + lists.lastnames_unclean)

    return '{} {}'.format(firstname, lastname)
