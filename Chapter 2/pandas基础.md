# pandas基础

```python
import numpy as np

import pandas as pd
```

需确认安装了`xlrd`、`xlwt`、`openpyxl`三个包

## 文件的读取与写入

### 文件读取

分别通过`pd.read_csv`、`pd.read_table`、`pd.read_excel`读取`csv`、`excel`、`txt`文件



第一行不作为列名、选定列作为索引、读取选定列、选定列转化为时间、选定行数

```python
pd.read_table('data/my_table.txt', header=None)
Out[10]: 
      0     1     2                3
0  col1  col2  col3             col4
1     2     a   1.4   apple 2020/1/1
2     3     b   3.4  banana 2020/1/2
3     6     c   2.5  orange 2020/1/5
4     5     d   3.2   lemon 2020/1/7

pd.read_csv('data/my_csv.csv', index_col=['col1', 'col2'])
Out[11]: 
           col3    col4      col5
col1 col2                        
2    a      1.4   apple  2020/1/1
3    b      3.4  banana  2020/1/2
6    c      2.5  orange  2020/1/5
5    d      3.2   lemon  2020/1/7

pd.read_table('data/my_table.txt', usecols=['col1', 'col2'])
Out[12]: 
   col1 col2
0     2    a
1     3    b
2     6    c
3     5    d

pd.read_csv('data/my_csv.csv', parse_dates=['col5'])
Out[13]: 
   col1 col2  col3    col4       col5
0     2    a   1.4   apple 2020-01-01
1     3    b   3.4  banana 2020-01-02
2     6    c   2.5  orange 2020-01-05
3     5    d   3.2   lemon 2020-01-07

pd.read_excel('data/my_excel.xlsx', nrows=2)
Out[14]: 
   col1 col2  col3    col4      col5
0     2    a   1.4   apple  2020/1/1
1     3    b   3.4  banana  2020/1/2
```

非空格作为分隔符时，txt文件的处理

```python
pd.read_table('data/my_table_special_sep.txt')
Out[15]: 
              col1 |||| col2
0  TS |||| This is an apple.
1    GQ |||| My name is Bob.
2         WT |||| Well done!
3    PT |||| May I help you?

pd.read_table('data/my_table_special_sep.txt',
              sep=' \|\|\|\| ', engine='python')

Out[16]: 
  col1               col2
0   TS  This is an apple.
1   GQ    My name is Bob.
2   WT         Well done!
3   PT    May I help you?
```

**sep使用的是正则表达式**

### 数据写入

通过`to_csv`、`to_excel`函数实现，txt则可以通过如`df_txt.to_csv('data/my_txt_saved.txt', sep='\t', index=False)`的方式实现

若要导出成`markdown`和`latex`语言，需要安装`tabulate`包，使用 `to_markdown` 和 `to_latex` 函数

## 基本数据结构

`pandas`中包括存储一维数据的`Series`和存储二维数据的`DataFrame`

### Series

由序列的值 `data` 、索引 `index` 、存储类型 `dtype` 、序列的名字 `name` 构成。索引也可以指定名字，默认为空。

```python
s = pd.Series(data = [100, 'a', {'dic1':5}],
              index = pd.Index(['id1', 20, 'third'], name='my_idx'),
              dtype = 'object',
              name = 'my_name')


s
Out[23]: 
my_idx
id1              100
20                 a
third    {'dic1': 5}
Name: my_name, dtype: object
```

**`object`为混合类型，同时`pandas`中纯文本也默认为这种类型（或者以`string`类型存储）**

获取可以通过`.`的方式

`.shape`表示序列长度

单个索引对应的值，可以通过 `[index_item]` 取出

### DataFrame

在 `Series` 的基础上增加了列索引，一个数据框可以由二维的 `data` 与行列索引来构造

```python'
data = [[1, 'a', 1.2], [2, 'b', 2.2], [3, 'c', 3.2]]

df = pd.DataFrame(data = data,
                  index = ['row_%d'%i for i in range(3)],
                  columns=['col_0', 'col_1', 'col_2'])


df
Out[32]: 
       col_0 col_1  col_2
row_0      1     a    1.2
row_1      2     b    2.2
row_2      3     c    3.2
```

或者列索引名到数据的映射来构造数据框，同时再加上行索引

```python
df = pd.DataFrame(data = {'col_0': [1,2,3], 'col_1':list('abc'),
                          'col_2': [1.2, 2.2, 3.2]},
                  index = ['row_%d'%i for i in range(3)])


df
Out[34]: 
       col_0 col_1  col_2
row_0      1     a    1.2
row_1      2     b    2.2
row_2      3     c    3.2
```

在`DataFrame`中提取使用列索引提取`Series`和`DataFrame`

```python
df['col_0']
Out[35]: 
row_0    1
row_1    2
row_2    3
Name: col_0, dtype: int64

df[['col_0', 'col_1']]
Out[36]: 
       col_0 col_1
row_0      1     a
row_1      2     b
row_2      3     c
```

获取值、行索引、列索引、变量类型、序列长度

```python
df.values
Out[37]: 
array([[1, 'a', 1.2],
       [2, 'b', 2.2],
       [3, 'c', 3.2]], dtype=object)

df.index
Out[38]: Index(['row_0', 'row_1', 'row_2'], dtype='object')

df.columns
Out[39]: Index(['col_0', 'col_1', 'col_2'], dtype='object')

df.dtypes # 返回的是值为相应列数据类型的Series
Out[40]: 
col_0      int64
col_1     object
col_2    float64
dtype: object

df.shape
Out[41]: (3, 3)
```

通过 `.T` 可以把 `DataFrame` 进行转置

## 常用基本函数

后续将使用`learn_pandas.csv` 虚拟数据集

首先进行导入，进行列选择

```
df = pd.read_csv('data/learn_pandas.csv')

In [44]: df.columns
Out[44]: 
Index(['School', 'Grade', 'Name', 'Gender', 'Height', 'Weight', 'Transfer',
       'Test_Number', 'Test_Date', 'Time_Record'],
      dtype='object')
      
df = df[df.columns[:7]]
```

### 汇总函数

`head, tail` 函数分别表示返回表或者序列的前 `n` 行和后 `n` 行，其中 `n` 默认为5

```
df.head(2)
Out[46]: 
                          School     Grade            Name  Gender  Height  Weight Transfer
0  Shanghai Jiao Tong University  Freshman    Gaopeng Yang  Female   158.9    46.0        N
1              Peking University  Freshman  Changqiang You    Male   166.5    70.0        N

In [47]: df.tail(3)
Out[47]: 
                            School      Grade            Name  Gender  Height  Weight Transfer
197  Shanghai Jiao Tong University     Senior  Chengqiang Chu  Female   153.9    45.0        N
198  Shanghai Jiao Tong University     Senior   Chengmei Shen    Male   175.3    71.0        N
199            Tsinghua University  Sophomore     Chunpeng Lv    Male   155.7    51.0        N
```

`info`, `describe` 分别返回表的 信息概况和表中数值列对应的主要统计量 

```python
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   School    200 non-null    object 
 1   Grade     200 non-null    object 
 2   Name      200 non-null    object 
 3   Gender    200 non-null    object 
 4   Height    183 non-null    float64
 5   Weight    189 non-null    float64
 6   Transfer  188 non-null    object 
dtypes: float64(2), object(5)
memory usage: 11.1+ KB

In [49]: df.describe()
Out[49]: 
           Height      Weight
count  183.000000  189.000000
mean   163.218033   55.015873
std      8.608879   12.824294
min    145.400000   34.000000
25%    157.150000   46.000000
50%    161.900000   51.000000
75%    167.500000   65.000000
max    193.900000   89.000000
```

**上述两函数展示的信息较少，列较多的情况下，可使用 [pandas-profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html) 包**

### 统计特征函数

均值、最大值、分位数、非缺失值个数、最大值对应索引、聚合

```python
df_demo = df[['Height', 'Weight']]

df_demo.mean()
Out[51]: 
Height    163.218033
Weight     55.015873
dtype: float64

df_demo.max()
Out[52]: 
Height    193.9
Weight     89.0
dtype: float64

df_demo.quantile(0.75)
Out[53]: 
Height    167.5
Weight     65.0
Name: 0.75, dtype: float64

df_demo.count()
Out[54]: 
Height    183
Weight    189
dtype: int64

df_demo.idxmax() # idxmin是对应的函数
Out[55]: 
Height    193
Weight      2
dtype: int64

df_demo.mean(axis=1).head() # 在这个数据集上体重和身高的均值并没有意义
# 默认为0代表逐列聚合，如果设置为1则表示逐行聚合
Out[56]: 
0    102.45
1    118.25
2    138.95
3     41.00
4    124.00
dtype: float64
```

### 唯一值函数

唯一值、唯一值个数、唯一值和对应频数

```python
df['School'].unique()
Out[57]: 
array(['Shanghai Jiao Tong University', 'Peking University',
       'Fudan University', 'Tsinghua University'], dtype=object)

df['School'].nunique()
Out[58]: 4

df['School'].value_counts()
Out[59]: 
Tsinghua University              69
Shanghai Jiao Tong University    57
Fudan University                 40
Peking University                34
Name: School, dtype: int64
```

### 替换函数

以下均以`Series`为例

数据编码通过`replace`函数实现，可以通过字典构造，或者传入两个列表来进行替换

```python
df['Gender'].replace({'Female':0, 'Male':1}).head()
Out[67]: 
0    0
1    1
2    1
3    0
4    1
Name: Gender, dtype: int64

df['Gender'].replace(['Female', 'Male'], [0, 1]).head()
Out[68]: 
0    0
1    1
2    1
3    0
4    1
Name: Gender, dtype: int64
```

方向替换可以通过指定 `method` 参数实现，参数为 `ffill` 则为用前面一个最近的未被替换的值进行替换， `bfill` 则使用后面最近的未被替换的值进行替换。

```python
s = pd.Series(['a', 1, 'b', 2, 1, 1, 'a'])

# 只替换1和2
s.replace([1, 2], method='ffill')
Out[70]: 
0    a
1    a
2    b
3    b
4    b
5    b
6    a
dtype: object

s.replace([1, 2], method='bfill')
Out[71]: 
0    a
1    b
2    b
3    a
4    a
5    a
6    a
dtype: object
```

**正则替换一般使用`str.replace`实现，因为`replace`对于`string`类型还存在bug**

逻辑替换包括了 `where` 和 `mask` ，这两个函数是完全对称的： `where` 函数在传入条件为 `False` 的对应行进行替换，而 `mask` 在传入条件为 `True` 的对应行进行替换，当不指定替换值时，替换为缺失值

```python
s = pd.Series([-1, 1.2345, 100, -50])

In [73]: s.where(s<0)
Out[73]: 
0    -1.0
1     NaN
2     NaN
3   -50.0
dtype: float64

In [74]: s.where(s<0, 100)
Out[74]: 
0     -1.0
1    100.0
2    100.0
3    -50.0
dtype: float64

In [75]: s.mask(s<0)
Out[75]: 
0         NaN
1      1.2345
2    100.0000
3         NaN
dtype: float64

In [76]: s.mask(s<0, -50)
Out[76]: 
0    -50.0000
1      1.2345
2    100.0000
3    -50.0000
dtype: float64
```

### 排序函数

分为`sort_values`值排序和`sort_index`索引排序

建立索引

```python
df_demo = df[['Grade', 'Name', 'Height',
              'Weight']].set_index(['Grade','Name'])
```

升序降序

```python
df_demo.sort_values('Height').head()
Out[84]: 
                         Height  Weight
Grade     Name                         
Junior    Xiaoli Chu      145.4    34.0
Senior    Gaomei Lv       147.3    34.0
Sophomore Peng Han        147.8    34.0
Senior    Changli Lv      148.7    41.0
Sophomore Changjuan You   150.5    40.0

df_demo.sort_values('Height', ascending=False).head()
Out[85]: 
                        Height  Weight
Grade    Name                         
Senior   Xiaoqiang Qin   193.9    79.0
         Mei Sun         188.9    89.0
         Gaoli Zhao      186.5    83.0
Freshman Qiang Han       185.3    87.0
Senior   Qiang Zheng     183.9    87.0
```

多列排序

```python
df_demo.sort_values(['Weight','Height'],ascending=[True,False]).head()
Out[86]: 
                       Height  Weight
Grade     Name                       
Sophomore Peng Han      147.8    34.0
Senior    Gaomei Lv     147.3    34.0
Junior    Xiaoli Chu    145.4    34.0
Sophomore Qiang Zhou    150.5    36.0
Freshman  Yanqiang Xu   152.4    38.0
```

索引排序（元素的值在索引中，自行定义），使用参数`level`

```python
df_demo.sort_index(level=['Grade','Name'],ascending=[True,False]).head()
Out[87]: 
                        Height  Weight
Grade    Name                         
Freshman Yanquan Wang    163.5    55.0
         Yanqiang Xu     152.4    38.0
         Yanqiang Feng   162.3    51.0
         Yanpeng Lv        NaN    65.0
         Yanli Zhang     165.1    52.0
```

### apply方法

常用于 `DataFrame` 的行迭代或者列迭代，`axis` 含义与统计聚合函数一致， `apply` 的参数往往是一个以序列为输入的函数。

自定义求平均

```python
df_demo = df[['Height', 'Weight']]

def my_mean(x):
    res = x.mean()
    return res


df_demo.apply(my_mean)
Out[90]: 
Height    163.218033
Weight     55.015873
dtype: float64

df_demo.apply(lambda x:x.mean())
Out[91]: 
Height    163.218033
Weight     55.015873
dtype: float64
```

逐行

```python
df_demo.apply(lambda x:x.mean(), axis=1).head()
Out[92]: 
0    102.45
1    118.25
2    138.95
3     41.00
4    124.00
dtype: float64
```

偏离均值总和

```python
df_demo.apply(lambda x:(x-x.mean()).abs().mean())
Out[93]: 
Height     6.707229
Weight    10.391870
dtype: float64

df_demo.mad()
Out[94]: 
Height     6.707229
Weight    10.391870
dtype: float64
```

**`apply`自由度很高，但是性能较差，一般非自定义需求情境下不优先使用`apply`**

## 窗口对象

### 滑窗对象

可通过聚合函数功能进行计算，最后即为当前行所在元素

均值、求和、相关系数、协方差计算

```python
s = pd.Series([1,2,3,4,5])

roller = s.rolling(window = 3)

roller
Out[97]: Rolling [window=3,center=False,axis=0]

roller.mean()
Out[98]: 
0    NaN
1    NaN
2    2.0
3    3.0
4    4.0
dtype: float64

roller.sum()
Out[99]: 
0     NaN
1     NaN
2     6.0
3     9.0
4    12.0
dtype: float64

s2 = pd.Series([1,2,6,16,30])

roller.cov(s2)
Out[101]: 
0     NaN
1     NaN
2     2.5
3     7.0
4    12.0
dtype: float64

roller.corr(s2)
Out[102]: 
0         NaN
1         NaN
2    0.944911
3    0.970725
4    0.995402
dtype: float64
```

自定义函数

```python
roller.apply(lambda x:x.mean())
Out[103]: 
0    NaN
1    NaN
2    2.0
3    3.0
4    4.0
dtype: float64
```

向前取值、向前作差、向前计算增长率(比例-100%)

```python
s = pd.Series([1,3,6,10,15])

s.shift(2)
Out[105]: 
0    NaN
1    NaN
2    1.0
3    3.0
4    6.0
dtype: float64

s.diff(3)
Out[106]: 
0     NaN
1     NaN
2     NaN
3     9.0
4    12.0
dtype: float64

s.pct_change()
Out[107]: 
0         NaN
1    2.000000
2    1.000000
3    0.666667
4    0.500000
dtype: float64

s.shift(-1)
Out[108]: 
0     3.0
1     6.0
2    10.0
3    15.0
4     NaN
dtype: float64

s.diff(-2)
Out[109]: 
0   -5.0
1   -7.0
2   -9.0
3    NaN
4    NaN
dtype: float64
```

### 扩张窗口

与滑动相对应，总数变化

```python
s = pd.Series([1, 3, 6, 10])

s.expanding().mean()
Out[115]: 
0    1.000000
1    2.000000
2    3.333333
3    5.000000
dtype: float64
```

`cummax`：累计最大，`.expanding().max()`

`cumsum`：累计求和，`.expanding().sum()`

`cumprod`：累计相乘，`.expanding().prod()`

## 练习

### Ex1：口袋妖怪数据集

现有一份口袋妖怪的数据集，下面进行一些背景说明：

- `#` 代表全国图鉴编号，不同行存在相同数字则表示为该妖怪的不同状态
- 妖怪具有单属性和双属性两种，对于单属性的妖怪， `Type 2` 为缺失值
- `Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed` 分别代表种族值、体力、物攻、防御、特攻、特防、速度，其中种族值为后6项之和

```
In [116]: df = pd.read_csv('data/pokemon.csv')

In [117]: df.head(3)
Out[117]: 
   #       Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed
0  1  Bulbasaur  Grass  Poison    318  45      49       49       65       65     45
1  2    Ivysaur  Grass  Poison    405  60      62       63       80       80     60
2  3   Venusaur  Grass  Poison    525  80      82       83      100      100     80
```

1. 对 `HP, Attack, Defense, Sp. Atk, Sp. Def, Speed` 进行加总，验证是否为 `Total` 值。
2. 对于 `#` 重复的妖怪只保留第一条记录，解决以下问题：

+ 求第一属性的种类数量和前三多数量对应的种类

+ 求第一属性和第二属性的组合种类

+ 求尚未出现过的属性组合

3. 按照下述要求，构造 `Series` ：

+ 取出物攻，超过120的替换为 `high` ，不足50的替换为 `low` ，否则设为 `mid`

+ 取出第一属性，分别用 `replace` 和 `apply` 替换所有字母为大写

+ 求每个妖怪六项能力的离差，即所有能力中偏离中位数最大的值，添加到 `df` 并从大到小排序

### Ex2：指数加权窗口

1. 作为扩张窗口的 `ewm` 窗口

在扩张窗口中，用户可以使用各类函数进行历史的累计指标统计，但这些内置的统计函数往往把窗口中的所有元素赋予了同样的权重。事实上，可以给出不同的权重来赋给窗口中的元素，指数加权窗口就是这样一种特殊的扩张窗口。

其中，最重要的参数是 `alpha` ，它决定了默认情况下的窗口权重为$wi=(1−α)^i,i \in {0,1,...,t}$，其中$i=t$ 表示当前元素，$i=0$ 表示序列的第一个元素。

从权重公式可以看出，离开当前值越远则权重越小，若记原序列为 `x` ，更新后的当前元素为 yt ，此时通过加权公式归一化后可知：
$$
\begin{equation*}
\begin{split}
y_t&=\frac{\sum^t_{i=0}\omega_ix_{t-i}}{\sum^t_{i=0}\omega_i}\\
&=\frac{x_t+(1-\alpha)x_{t-1}+(1-\alpha)x^2_{t-2}+(1-\alpha)x^t_{0}}{1+(1-\alpha)+(1-\alpha)^2+...+(1-\alpha)^t}
\end{split}
\end{equation*}
$$


对于 `Series` 而言，可以用 `ewm` 对象如下计算指数平滑后的序列：

```
In [118]: np.random.seed(0)

In [119]: s = pd.Series(np.random.randint(-1,2,30).cumsum())

In [120]: s.head()
Out[120]: 
0   -1
1   -1
2   -2
3   -2
4   -2
dtype: int32

In [121]: s.ewm(alpha=0.2).mean().head()
Out[121]: 
0   -1.000000
1   -1.000000
2   -1.409836
3   -1.609756
4   -1.725845
dtype: float64
```

请用 `expanding` 窗口实现。

2. 作为滑动窗口的 `ewm` 窗口

从第1问中可以看到， `ewm` 作为一种扩张窗口的特例，只能从序列的第一个元素开始加权。现在希望给定一个限制窗口 `n` ，只对包含自身的最近的 `n` 个元素作为窗口进行滑动加权平滑。请根据滑窗函数，给出新的$w_i$与$y_t$的更新公式，并通过 `rolling` 窗口实现这一功能。
