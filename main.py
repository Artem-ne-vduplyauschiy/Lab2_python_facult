import numpy as np
from PIL import Image
from numpy.core._multiarray_umath import ndarray  # оно само, я его не добавлял
import os
import re
from matplotlib import pyplot as plt

path = input('Введите путь: ')
pattern = r"\.\w{3}$"
if path:
    if os.path.exists(path):
        if re.search(pattern, path):
            if path.endswith('.png'):
                img_colored: ndarray = np.asarray(
                    Image.open(path))  # тоже само сгенерировалось вместо предлагаемого варианта
                print('Минимальная яркость по красному каналу', img_colored[:, :, 0].min(),
                      '\nМаксимальная яркость по красному каналу', img_colored[:, :, 0].max(),
                      '\nСредняя яркость по красному каналу', round(img_colored[:, :, 0].mean(), 3),
                      '\nМинимальная яркость по зелёному каналу', img_colored[:, :, 1].min(),
                      '\nМаксимальная яркость по зелёному каналу', img_colored[:, :, 1].max(),
                      '\nСредняя яркость по зелёному каналу', round(img_colored[:, :, 1].mean(), 3),
                      '\nМинимальная яркость по синему каналу', img_colored[:, :, 2].min(),
                      '\nМаксимальная яркость по синему каналу', img_colored[:, :, 2].max(),
                      '\nСредняя яркость по синему каналу', round(img_colored[:, :, 2].mean(), 3),
                      '\nРазмерность изображения', img_colored.shape)
                img_gray = img_colored * [0.299, 0.587, 0.114]
                img_gray = img_gray.sum(axis=2)
                img_gray = img_gray.astype(np.uint8)
                # print(round(arr.min(), 3), round(arr.max(), 3), round(arr.mean(), 3), arr.shape)
                img_gray = Image.fromarray(img_gray)
                img_gray.save('Lena_grayscaled.png')
                img_gray2: ndarray = np.asarray(Image.open('Lena_grayscaled.png'))
                img_thresholded3 = img_gray2.copy()
                img_thresholded3[img_thresholded3 < 50] = 0
                img_thresholded3 = Image.fromarray(img_thresholded3)
                img_thresholded3.save('Lena_thresholded.png')
                # print(round(arr3.min(), 3), round(arr3.max(), 3), round(arr3.mean(), 3), arr3.shape)
                plt.hist(img_thresholded3)
                plt.title('Гистограмма яркости')
                plt.xlabel('Яркость')
                plt.ylabel('Частота')
                plt.show()
            else:
                print('Неверное расширение файла')
        else:
            print('Хоть такой путь и есть, но имя файла не указано ')
    else:
        print('Путь указан неверно или такого файла с таким расширением по указанному пути нет')
