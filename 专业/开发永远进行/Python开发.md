# Python开发

## 函数

### 1 如何在Python方法中加入可选参数

如下所示：

```python
def printA(name = "Jack"):
	print(name)
printA() # => Jack
printA("David") # => David 
```

加入可选参数后，未包含可选参数的方法就不会报错



## 类型转换

### 1 转字符串

```python
str()
```

## 字符串

### 1 字符串替换

如下所示:

```python
original_string = "Hello, world!"
char_to_remove = ","
modified_string = original_string.replace(char_to_remove, "")
print(modified_string)  # 输出: Hello world!
```

## 文件

### 1 解析json文件

```python
with open(jsonpath,'r', encoding='utf-8') as file:
    self.jsonObject = json.load(file)
```

## 字典

### 1 创建一个字典对象

```python
data = {
    "position": {
        "x": -400,
        "y": -140
    },
    "sizes": {
        "width": 100,
        "height": 80
    }
}
```

### 2 字典充当Map

Python的字典的功能类似于其他编程语言中的Map，并且字典的值可以是函数与类的实例



### 3 创建一个空的字典

```python
empty_dict = {}
```



## 集合

### 1 创建集合

使用大括号创建集合

```python
# 创建一个空集合  
empty_set = set()
  
# 创建一个包含多个元素的集合  
my_set = {1, 2, 3, 4, 5}  
  
# 创建一个包含字符串元素的集合  
string_set = {'apple', 'banana', 'cherry'}  
  
print(empty_set)  # 输出：set()  
print(my_set)      # 输出：{1, 2, 3, 4, 5}  
print(string_set)  # 输出：{'cherry', 'banana', 'apple'}
```



使用set（）函数创建集合

```python
# 使用set()函数创建一个空集合  
empty_set = set()  
  
# 使用set()函数创建一个包含多个元素的集合  
my_set = set([1, 2, 2, 3, 4, 4, 5])  # 注意，集合中的元素不会重复  
  
# 使用set()函数创建一个包含字符串元素的集合  
string_set = set(['apple', 'banana', 'banana', 'cherry'])  # 注意，集合中的元素不会重复  
  
print(empty_set)  # 输出：set()  
print(my_set)      # 输出：{1, 2, 3, 4, 5}  
print(string_set)  # 输出：{'cherry', 'banana', 'apple'}
```



## For使用

### 1 获取item和index

```python
my_list = ['apple', 'banana', 'cherry', 'date']  
  
for index, value in enumerate(my_list):  
    print(f"索引: {index}, 值: {value}")
```

