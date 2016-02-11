"""Generate random English names similar to Benedict Cumberbatch."""

import argparse
import cumberbatch

def main():
    parser = argparse.ArgumentParser("python -m cumberbatch")
    parser.description = __doc__
    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument('--first', action='store_true', help="Only generate a first name.")
    exclusive.add_argument('--last', action='store_true', help="Only generate a last name.")
    parser.add_argument('--nsfw', action='store_true', help="Allow NSFW names.")
    opts = parser.parse_args()
    clean = not opts.nsfw
    if opts.first:
        print(cumberbatch.first(clean=clean))
    elif opts.last:
        print(cumberbatch.last(clean=clean))
    else:
        print(cumberbatch.full(clean=clean))

if __name__ == '__main__':
    main()

