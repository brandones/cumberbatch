""" test_cumberbatch.py

    Unit tests for cumberbatch
"""

import unittest
import cumberbatch

class TestCumberbatch(unittest.TestCase):

    def test_returns_strings(self):
        self.assertIsInstance(cumberbatch.first(), str)
        self.assertIsInstance(cumberbatch.last(), str)
        self.assertIsInstance(cumberbatch.full(), str)

        self.assertIsInstance(cumberbatch.first(clean=False), str)
        self.assertIsInstance(cumberbatch.last(clean=False), str)
        self.assertIsInstance(cumberbatch.full(clean=False), str)

    def test_full_generates_two_words_with_space(self):
        for i in range(100):
            self.assertRegexpMatches(cumberbatch.full(), '\a* \a*')
            self.assertRegexpMatches(cumberbatch.full(clean=False), '\a* \a*')

    def test_no_dirty_words_if_clean(self):
        for i in range(100):
            self.assertNotIn(cumberbatch.first(), cumberbatch.Lists.firstnames_unclean)
            self.assertNotIn(cumberbatch.last(), cumberbatch.Lists.lastnames_unclean)

            fullname = cumberbatch.full()
            self.assertNotIn(fullname, cumberbatch.Lists.fullnames_unclean)
            (full_first, full_last) = fullname.split(' ')
            self.assertNotIn(full_first, cumberbatch.Lists.firstnames_unclean)
            self.assertNotIn(full_last, cumberbatch.Lists.lastnames_unclean)

    def test_clean_false_produces_dirty_words(self):
        found_first = False
        for i in range(1000):
            found_first = cumberbatch.first(clean=False) in cumberbatch.Lists.firstnames_unclean
            if found_first:
                break
        self.assertTrue(found_first)

        found_last = False
        for i in range(1000):
            found_last = cumberbatch.last(clean=False) in cumberbatch.Lists.lastnames_unclean
            if found_last:
                break
        self.assertTrue(found_last)

        found_full_dirty_part = False
        found_full = False
        for i in range(100000):
            fullname = cumberbatch.full(clean=False)
            (full_first, full_last) = fullname.split(' ')
            if not found_full_dirty_part:
                found_full_dirty_part = (full_first in cumberbatch.Lists.firstnames_unclean or
                                         full_last in cumberbatch.Lists.lastnames_unclean)
            if not found_full:
                found_full = fullname in cumberbatch.Lists.fullnames_unclean
            if found_full_dirty_part and found_full:
                break
        self.assertTrue(found_full_dirty_part)
        self.assertTrue(found_full)
