## Pandas란?

Series와 Data Frame 자료구조(빅데이터 분석에서 높은 수준으 성능을 보임)로 데이터를 다룰 수 있도록 해줌

## 데이터 프레임 이론

- 데이터프레임에서 특정한 데이터만 골라내는 것을 `인덱싱(indexing)`이라고 한다.
- 인덱싱에 관련하여 [Indexing tutorial](https://datascienceschool.net/view-notebook/704731b41f794b8ea00768f5b0904512/) 을 참고할 만 하다.

## Read data from csv

```py
import pandas as pd
df = pd.read_csv('/my_drive/raw_data.csv', '\n', header=None)
type(df)
```

## 데이터 살펴보기

```py
head_df = df.head() # 상위 5개 데이터
tail_df = df.tail() # 하위 5개 데이터
```

## 데이터 얻기

```py
head_df.values # Return: class 'numpy.ndarray'
```

## Dict list into dataframe

```py
parsed_list = list(parsed_df) # parsed_list는 dict element로 구성된 list
df = pd.DataFrame(parsed_list)
```

## Dataframe.map 특정 Series 에 대하여, custom function 처리 하기

```py
# date field 전처리
import datetime
mock_df['date'] = mock_df['date'].map(lambda d: datetime.datetime.strptime(d['$date'], '%Y-%m-%dT%H:%M:%S.%fZ'))
mock_df
```

## 특정 column drop하기

```py
df.drop(columns=['_id'], axis=1)
```

## 특정 Column 값들 선택하기

```py
df['gasusage_ems_a'].values.tolist()
```

## iloc, loc

- iloc: integer position을 통해서 값을 찾는다.
- loc: label을 통해서 값을 찾는다.

## Get delta value

```python
arr = df.gasusage_ems_a.diff().values.tolist()
# Fill Nan with 0
df['DataFrame Column'] = df['DataFrame Column'].fillna(0)
```

## Extract subdataframe

```python
df[['a', 'b', 'c']]
```
