# matplotlib 기초

### 기본 차트 그리기

```
x = np.arange(0, 11)
y1 = np.array([e**1 for e in x])
y2 = np.array([e**2 for e in x])

pyplot.plot(x, y1)
pyplot.show()
```

### 여러 차트 그리기 하나의 window - subplot

- 첫번째 digit: 열의 수
- 두번째 digit: 행의 수
- 세번쨰 digit: n개의 자리 중 자리번호

```
plt.subplot(311)
plt.plot(x, y1)

plt.subplot(312)
plt.plot(x, y2)
plt.show()
```

### 여러 차트 그리기 다수 window - figure

```
plt.figure(1)
plt.plot(x, y1)

plt.figure(2)
plt.plot(x, y2)
plt.show()
```

# Pandas Dataframe으로 부터 그래프 그리기

출처
https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot

### Sample data for examples

```py
import pandas as pd

df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})
```

### Scatter plot of two columns

```py
import matplotlib.pyplot as plt
import pandas as pd

# a scatter plot comparing num_children and num_pets
df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
plt.show()
```

### Bar plot of column values

```py
import matplotlib.pyplot as plt
import pandas as pd

# a simple line plot
df.plot(kind='bar',x='name',y='age')
```
