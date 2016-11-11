python2--->ConfigParser 
python3 -->configparser
方法倒是没什么变化，所以有个兼容性的写法是：
```
try:
    import ConfigParser
except:
    import configparser as ConfigParser
```
初始化类，并加载配置文件
```
conf = ConfigParser.ConfigParser()
conf.read("settings.ini")
```
获取配置文件中所有的 sections的名称
```
sectctions = conf.sections()
```
返回结果是：
```
['sec_a', 'sec_b']

```
获取指定sections中所有的options:
```
options = conf.options("sec_b")
```
返回结果:
```
['b_key1', 'b_key2', 'b_key3', 'b_key4']

```
得到指定section的所有键值对
```
kvs = conf.items("sec_b")
```
返回结果:
```
[('b_key1', '121'), ('b_key2', 'b_value2'), ('b_key3', '$r'), ('b_key4', '127.0.0.1')]
```

得到指定section,option的值
```
str_vaule = conf.get("sec_b", 'b_key2')
print(str_vaule)
print(type(str_vaule))
```
返回结果:
```
b_value2
<type 'str'>
```
- get还有三种方式        
  - getint--获取整型值
  - getfloat--获取浮点数
  - getboolean--获取bool类型

- ini文件中使用变量 和 %(使用的变量)s

-------------------
ini文件使用数组
ini没有内置数组，要使用数组则在定义的时候以逗号分隔,解析时使用python字符串的spilt方法，分割成数组
such:
配置文件：
```
# settings.ini
[sec_a]
a_key1 = qu,yuan,ququu
```
解析：
```
str_vaule = conf.get("sec_a", 'a_key1').split(",")
print(str_vaule)
```
结果:
```
['qu', 'yuan', 'ququu']
```

------------
ini文件使用字典
ini使用字典，定义一个sections，字典的键值对在里面定义
such:
配置文件：
```
# settings.ini
[db]
host = 127.0.0.1
port:3306
dbname:qy
```
解析：
```
db = dict(conf.items("db"))
print(db)
```
结果:
```
{'host': '127.0.0.1', 'port': '3306', 'dbname': 'qy'}
```

