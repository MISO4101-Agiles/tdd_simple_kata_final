__author__ = 'Luis_Sebastian_Talero'


class Statistics:
    @staticmethod
    def gen_statistics(sequence):
        result_array = []
        if not sequence:
            result_array.append(0)
            result_array.append(0)
            return result_array
        else:
            nums = sequence.split(",")
            result_array.append(nums.__len__())
            return result_array

