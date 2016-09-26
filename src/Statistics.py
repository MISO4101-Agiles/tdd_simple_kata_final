__author__ = 'Luis_Sebastian_Talero'


class Statistics:
    @staticmethod
    def gen_statistics(sequence):
        result_array = [1]
        if not sequence:
            result_array[0] = 0
            result_array[1] = 0
            return result_array
        else:
            nums = sequence.split(",")
            result_array[0] = nums.__len__()
            return result_array

