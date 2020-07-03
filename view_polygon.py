import json
import numpy as np
import matplotlib.pyplot as plt


class DataForPolygons:
    "For builds  polygon"

    def __init__(self, dataset_file):
        # List points x
        self.x = []
        # List points y
        self.y = []
        # List read file
        self.data = []

        # Name receive file
        self.file = dataset_file

        try:
            with open(self.file, 'r') as dataset:
                self.data = json.load(dataset)
                for coord in self.data:
                    self.x.append(coord[0])
                for coord in self.data:
                    self.y.append(coord[1])
        except FileNotFoundError as e:
            print('Файл или директория не существует', e)

        # Number of vertices
        self.V = len(self.data)
    def draw_polygon_no_verification(self):
        """
        Draw polygon no verification
        :return: no verification draw
        """
        plt.plot(self.x, self.y, color='blue', marker='o')
        for i in range(len(self.data)):
            x = self.data[i][0]
            y = self.data[i][1]
            plt.text(x, y, i, fontsize=12)
        return plt.show()

    def draw_polygon_verification(self):
        """

        :return: verification draw
        """
        try:
            # Centre calc
            center_point = [np.sum(self.x) / self.V, np.sum(self.y) / self.V]
            # Angles
            angles = np.arctan2(self.x - center_point[0], self.y - center_point[1])
            # Sorted
            sort_tups = sorted([(i, j, k) for i, j, k in zip(self.x, self.y, angles)], key=lambda t: t[2])
            # todo Проверка, на одном наброе из json файле выдает ошибку пока закоментирована
            # if len(sort_tups) != len(set(sort_tups)):
            #     raise Exception('Получены две равные координаты')
            # Magic Block->=================================
            xx, yy, angles = zip(*sort_tups)
            xx, yy = list(xx), list(yy)
            xx.append(xx[0])
            yy.append(yy[0])
            # End Magic Block->=============================
            fig, ax = plt.subplots()
            ax.plot(xx, yy, color='blue', marker='o')
            for i in range(len(self.data)):
                x = self.data[i][0]
                y = self.data[i][1]
                plt.text(x, y, i, fontsize=12)
            return plt.show()
        except ValueError:
            print('Ошибка')
            return



if __name__ == '__main__':
    # В конструктор передать 'dataset1.json' либо 'dataset2.json'
    dataset1 = DataForPolygons('dataset1.json')
    dataset1.draw_polygon_verification()
    dataset2 = DataForPolygons('dataset2.json')
    dataset2.draw_polygon_verification()
