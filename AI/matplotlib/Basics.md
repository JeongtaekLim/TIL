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
