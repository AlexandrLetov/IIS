class Strategy:
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self, nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        print("Strategy 1 - bubble_sort")
        print(nums)

def selection_sort(nums):  
    # значение i соответствует тому, сколько значений было отсортировано
    for i in range(len(nums)):
        # Мы предполагаем, что первый элемент несортированного сегмента является наименьшим
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Поменять местами значения самого низкого несортированного элемента с первым несортированным
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    print("Strategy 2 - selection_sort")
    print(nums)

def insertion_sort(nums):  
    # Начнем со второго элемента, так как мы предполагаем, что первый элемент отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # И сохранить ссылку на индекс предыдущего элемента
        j = i - 1
        # Переместить все элементы отсортированного сегмента вперед, если они больше, чем элемент для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
    print("Strategy 3 - insertion_sort")
    print(nums)


if __name__ == "__main__":
    #random_list_of_nums = [5, 2, 1, 8, 4]
    random_list_of_nums = [5, 1, 2, 8, 4] 
    end_list_of_nums = [1, 2, 4, 5, 8]
    print('Исходный массив: ', random_list_of_nums) 
    strat0 = Strategy()
    strat1 = Strategy(selection_sort)
    strat2 = Strategy(insertion_sort)

    strat0.execute(random_list_of_nums)
    strat1.execute(random_list_of_nums)
    strat2.execute(random_list_of_nums)
