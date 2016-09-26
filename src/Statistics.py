__author__ = 'Luis_Sebastian_Talero'


class Statistics:
    @staticmethod
    def gen_statistics(sequence):
        if not sequence:
            return 0
        else:
            nums = sequence.split(",")
            if nums.__len__() == 1:
                return 1
            else:
                return 2
