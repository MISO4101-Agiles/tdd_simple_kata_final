from unittest import TestCase
from .Statistics import Statistics

__author__ = 'Luis_Sebastian_Talero'


class TestStatistics(TestCase):
    def test_gen_statistics(self):
        self.assertEqual(Statistics.gen_statistics(""), 0, "Empty String")
