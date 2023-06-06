#  В этот раз нам предстоит написать алгоритм, который сначала разработал Боер Мур в 1977
#  А в 1980 его доработал Хорспул
#  Принципы вроде бы те же, что и в алгоритме КМП,
#  но сравнивание элементов массива образца с искомым идёт с права налево
#  и если элементы не равны, то здесь появляется два условия с проверками:
#  в первом условии мы проверяем, есть ли не совпавший элемент с искомым в таблице значений.
#  Если есть, то мы сдвигаем искомый массив вправо на столько индексов,
#  сколько указано в таблице для соответствующего элемента.
#  Иначе если нет, то мы сдвигаем искомый массив на столько индексов,
#  сколько указано в таблице под индексом 0


def BMX(str1 : str, str2 : str) -> bool:
    pi = {'*': len(str2)}  # Д А Н Н Ы Е
    for i in range(- 2, - len(str2) - 1, - 1):
        if str2[i] in pi.keys():
            pass
        else:
            pi[str2[i]] = - (i + 1)
    def search(pi, str1, str2):
        i = len(str2) - 1
        j = i
        # print(str1[i], str2[j], 'z')
        while i < len(str1) - 1:
            print('str1[i]: ',str1[i],'str2[j]:', str2[j],'i: ', i,'j: ',j, 'begin')
            if str1[i] == str2[j]:
                print('if str1[i] == str2[j]:\n','str1[i]: ',str1[i],'str2[j]:', str2[j],'i: ', i,'j: ',j)
                i -= 1
                j -= 1
            else:
                if j == len(str2) - 1:
                    print('if j == len(str2) - 1:\n','str1[i]: ',str1[i],'str2[j]:', str2[j],'i: ', i,'j: ',j)
                    i += pi['*'] if str1[i] not in pi.keys() else pi[str1[i]]
                else:
                    print('if j != len(str2) - 1:\n', 'str1[i]: ',str1[i],'str2[j]:', str2[j],'i: ', i,'j: ',j)
                    i += pi[str2[j]]
            print('str1[i]: ',str1[i],'str2[j]:', str2[j],'i: ', i,'j: ',j, 'end')
            if j == 0:
                return True
        return False
    return search(pi, str1, str2)


print(BMX('большие метеоданные', 'данныел'))