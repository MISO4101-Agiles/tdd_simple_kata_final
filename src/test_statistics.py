from unittest import TestCase
from .Statistics import Statistics

__author__ = 'Luis_Sebastian_Talero'


class TestStatistics(TestCase):
    def test_gen_statistics_1_0(self):
        self.assertEqual(Statistics.gen_statistics(""), 0, "Empty String")

    def test_gen_statistics_1_1(self):
        self.assertEqual(Statistics.gen_statistics("1"), 1, "String 1")

    def test_gen_statistics_1_2(self):
        self.assertEqual(Statistics.gen_statistics("1,2"), 2, "String 2")

    def test_gen_statistics_1_3(self):
        self.assertEqual(Statistics.gen_statistics("1,2,3,4,5"), 5, "String +2")
