cumberbatch
###########

Generates names similar to "Benedict Cumberbatch"

The module benedict provides three functions: first, last, and full.
All three have an optional parameter "clean" which defaults true.
`clean=False` is passed, some of the results may not be child/boss friendly
(though most of them still will be, as in the use below).

Usage
*****

::
    >>> from cumberbatch import benedict
    >>> benedict.first()
    'Boilerdang'
    >>> benedict.last()
    'Cabbagepatch'
    >>> benedict.full()
    'Bombadil Coggleswort'
    >>> benedict.full(clean=False)
    'Barister Colonist'


Contributing
************

Feel free to fork me and create a pull request at
https://github.com/brandones/cumberbatch


