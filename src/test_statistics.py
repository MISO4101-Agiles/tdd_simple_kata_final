from unittest import TestCase
from .Statistics import Statistics

__author__ = 'Luis_Sebastian_Talero'


class TestStatistics(TestCase):

    # Iteración 1

    #   def test_gen_statistics_1_0(self):
    #       array = [0]
    #       self.assertEqual(Statistics.gen_statistics(""), array, "Empty String")

    #  def test_gen_statistics_1_1(self):
    #      array = [1]
    #      self.assertEqual(Statistics.gen_statistics("1"), array, "String 1")

    #    def test_gen_statistics_1_2(self):
    #        array = [2]
    #        self.assertEqual(Statistics.gen_statistics("1,2"), array, "String 2")

    #    def test_gen_statistics_1_3(self):
    #        array = [5]
    #        self.assertEqual(Statistics.gen_statistics("1,2,3,4,5"), array, "String +2")

    # Iteración 2

    #    def test_gen_statistics_2_0(self):
    #        array = [0, 0]
    #        self.assertEqual(Statistics.gen_statistics(""), array, "Empty String")

    #    def test_gen_statistics_2_1(self):
    #        array = [1, 1]
    #        self.assertEqual(Statistics.gen_statistics("1"), array, "String 1")

    #    def test_gen_statistics_2_2(self):
    #        array = [2, 1]
    #        self.assertEqual(Statistics.gen_statistics("1,2"), array, "String 2")

    #    def test_gen_statistics_2_3(self):
    #        array = [5, 2]
    #        self.assertEqual(Statistics.gen_statistics("2,3,4,5,6"), array, "String +2")

    # Iteración 3

    #    def test_gen_statistics_3_0(self):
    #        array = [0, 0, 0]
    #        self.assertEqual(Statistics.gen_statistics(""), array, "Empty String")

    #    def test_gen_statistics_3_1(self):
    #        array = [1, 1, 1]
    #        self.assertEqual(Statistics.gen_statistics("1"), array, "String 1")

    #    def test_gen_statistics_3_3(self):
    #        array = [2, 1, 2]
    #        self.assertEqual(Statistics.gen_statistics("1,2"), array, "String 2")

    #    def test_gen_statistics_3_3(self):
    #        array = [5, 2, 6]
    #        self.assertEqual(Statistics.gen_statistics("2,3,4,5,6"), array, "String +2")

    # Iteración 4

    def test_gen_statistics_4_0(self):
        array = [0, 0, 0, 0]
        self.assertEqual(Statistics.gen_statistics(""), array, "Empty String")

