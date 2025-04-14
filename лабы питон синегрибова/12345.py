import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target


class_labels = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
data['species'] = data['target'].map(class_labels)


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='sepal length (cm)', y='sepal width (cm)', hue='species', palette='Set1')
plt.title('Диаграмма рассеяния для набора данных Iris')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Ширина чашелистика (см)')
plt.legend(title='Вид')
plt.grid()
plt.show()