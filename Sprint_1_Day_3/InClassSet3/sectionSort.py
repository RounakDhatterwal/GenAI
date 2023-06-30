tupl = [64, 25, 12, 22, 11]

def selectionSort(tupl):
    for i in range(len(tupl)):
        min = i
        for j in range(i+1, len(tupl)):
            if tupl[j] < tupl[min]:
                min = j
        tupl[i], tupl[min] = tupl[min], tupl[i]

selectionSort(tupl)
print(tupl)