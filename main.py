import numpy as np
from PIL import Image
from numpy.core._multiarray_umath import ndarray  # оно само, я его не добавлял
import os
from matplotlib import pyplot as plt


path = input('Введите путь: ')
if path:
    if os.path.exists(path):
        if path.endswith('.png'):
            arr: ndarray = np.asarray(Image.open(path))  # тоже само сгенерировалось вместо предлагаемого варианта
            print(arr.min(), arr.max(), round(arr.mean(), 3), arr.shape)
            arr = arr*[0.299, 0.587, 0.114]
            arr = arr.sum(axis=2)
            arr = arr.astype(np.uint8)
            #print(round(arr.min(), 3), round(arr.max(), 3), round(arr.mean(), 3), arr.shape)
            img = Image.fromarray(arr)
            img.save('Lena_grayscaled.png')
            arr2: ndarray = np.asarray(Image.open('Lena_grayscaled.png'))
            arr3 = arr2.copy()
            arr3[arr3 < 50] = 0
            img = Image.fromarray(arr3)
            img.save('Lena_thresholded.png')
            #print(round(arr3.min(), 3), round(arr3.max(), 3), round(arr3.mean(), 3), arr3.shape)
            print(img.histogram())  # гистограмма от PIL
            #plt.hist(img) # вроде гистограмма так должна выглядеть
            #plt.xlabel('Яркость')
            #plt.ylabel('Частота')
            #plt.show()
        else:
            print('Неверное расширение файла')
    else:
        print('Файл не найден')
