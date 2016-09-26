from statistics import mean

__author__ = 'Luis_Sebastian_Talero'


class Statistics:
    @staticmethod
    def gen_statistics(sequence):
        result_array = []
        if not sequence:
            result_array.append(0)
            result_array.append(0)
            result_array.append(0)
            result_array.append(0)
            return result_array
        else:
            nums = sequence.split(",")
            nums_int = list(map(int, nums))
            min_number = min(i for i in nums_int if i >= 0)
            max_number = max(i for i in nums_int if i >= 0)
            if nums.__len__() == 1:
                result_array.append(1)
                result_array.append(min_number)
                result_array.append(max_number)
                result_array.append(mean(nums_int))
                return result_array


