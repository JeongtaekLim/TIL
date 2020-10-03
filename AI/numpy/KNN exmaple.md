# KNN 예제

```py
import numpy as np
import matplotlib.pyplot as plt

dataset = np.array([
    [3, 104],
    [2, 100],
    [1, 81],
    [101, 10],
    [99, 5],
    [98, 2],
])

labels = np.array(['Romance', 'Romance', 'Romance',
                   'Action', 'Action', 'Action'])

inX = np.array([25, 87])
```

## 두 점사이의 거리 구하기

- 무식한 방법

```
dist_func = lambda x: np.sqrt((x[0] - inX[0])**2 + (x[1] - inX[1])**2)
dist_list = np.array([dist_func(x) for x in dataset])
print(dist_list)
```

- numpy 활용방법

```
dist_list = np.sqrt(np.sum((inX - dataset) ** 2, axis=1))
```

## 가장 가까운 점 4개 찾기

```
sorted_dist_list = dist_list.argsort()
filtered_label_list = labels[sorted_dist_list[:4]]
element_list, count_list = np.unique(filtered_label_list, return_counts=True)
```
