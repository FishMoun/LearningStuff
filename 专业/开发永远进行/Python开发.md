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

