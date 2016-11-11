
参考[阮一峰的YAML 语言教程](http://www.ruanyifeng.com/blog/2016/07/yaml.html?f=tt),将其中javasc转为了的python实现

#### 一、简介

YAML 语言（发音 /?j?m?l/ ）的设计目标，就是方便人类读写。它实质上是一种通用的数据串行化格式。

它的基本语法规则如下:
- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，只允许使用空格。
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可  

\# 表示注释，从这个字符一直到行尾，都会被解析器忽略。

YAML 支持的数据结构有三种:
- 对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
- 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
- 纯量（scalars）：单个的、不可再分的值

#### 二、对象
对象的一组键值对，使用冒号结构表示:
```
animal: pets
```
转为Python如下:
```
{'animal': 'pets'}
```
Yaml 也允许另一种写法，将所有键值对写成一个行内对象：
```
hash: { name: Steve, foo: bar } 
```
转为Python如下:
```
{'hash': {'foo': 'bar', 'name': 'Steve'}}
```

#### 三、数组
一组连词线开头的行，构成一个数组:
```
- Cat
- Dog
- Goldfish
```
转为Python如下:
```
['Cat', 'Dog', 'Goldfish']
```
数据结构的子成员是一个数组，则可以在该项下面缩进一个空格:
```
-
 - Cat
 - Dog
 - Goldfish
```
转为Python如下:
```
[['Cat', 'Dog', 'Goldfish']]
```
数组也可以采用行内表示法:
```
animal: [Cat, Dog]
```
也可以用这种数组写法：
```
animal:
  - Cat
  - Dog

```
转为Python如下:
```
{'animal': ['Cat', 'Dog']}
```

##### 四、复合结构
对象和数组可以结合使用，形成复合结构:
```
languages:
 - Ruby
 - Perl
 - Python 
websites:
 YAML: yaml.org 
 Ruby: ruby-lang.org 
 Python: python.org 
 Perl: use.perl.org 
```
转为Python如下:
```
{
    'languages': ['Ruby', 'Perl', 'Python'], 
    'websites': 
    {
        'Python': 'python.org', 
        'YAML': 'yaml.org', 
        'Ruby': 'ruby-lang.org',
        'Perl': 'use.perl.org'
    }
}
```

#### 五、纯量 

yaml写法 | python数据类型 | 说明
---|---|---
`number: 12.30` | `{'languages': 12.1}` |  数值直接以字面量的形式表示
`isSet: true` | `{'isSet': True}` |  布尔值用`true`和`false`表示
`parent: ~ ` | `{'parent': None}` |  `null`用`~`表示
`iso8601: 2001-12-14t21:59:43.10-05:00 ` | `{'iso8601': datetime.datetime(2001, 12, 15, 2, 59, 43, 100000)}` | 时间采用 `ISO8601` 格式
`date: 1976-07-31` | `{'date': datetime.date(1976, 7, 31)}` | 日期采用复合 iso8601 格式的年、月、日表示
`e: !!str 123` | {'e': '123'} | YAML 允许使用两个感叹号，强制转换数据类型


#### 六、字符串
字符串是最常见，也是最复杂的一种数据类型，字符串默认不使用引号表示：
```
str: string
```
转为Python如下:
```
{'str': 'string'}
```

如果字符串之中包含空格或特殊字符，需要放在引号之中(貌似不用括号也没问题，不过这里这么说了，就加下吧):
```
str: This is string
```
转为Python如下:
```
{'str': 'This is string'}
{'str': 'This is string'}
```
单引号和双引号都可以使用，但是==双引号不会对特殊字符转义==
```
s1: 'context\nstring'
s2: "context\nstring"
```
转为Python如下:
```
{
    's1': 'context\\nstring',
    's2': 'context\nstring',
}
```
单引号之中如果还有单引号，必须连续使用两个单引号转义:
```
str: 'labor''s day' 
# 这种也行 str: "labor's day"
```

转为Python如下:
```
{'str': "labor's day"}
```
字符串可以写成多行，从第二行开始，必须有一个单空格缩进。换行符会被转为空格：
```
str: str1
  str2
  str3
```
转为Python如下:
```
{'str': 'str1 str2 str3'}
```


多行字符串可以使用`|`保留换行符，也可以使用`>`折叠换行(结尾处显示一个换行，其余显示成空格):
```
this: |
  Foo
  Bar
that: >
  Foo
  Bar
```
转为Python如下:
```
{'this': 'Foo\nBar\n', 'that': 'Foo Bar\n'}
```
`+`表示保留文字块末尾的换行，`-`表示删除字符串末尾的换行：
```
s1: |
  Foo
s2: >
 Foo

s3: |+
  Foo


s4: |-
  Foo

```
转为Python如下(为了阅读的顺畅，我将格式调整了一下):
```
{
  's1': 'Foo\n',
  's2': 'Foo\n',
  's3': 'Foo\n\n\n',
  's4': 'Foo'
}
```
字符串之中可以插入 `HTML` 标记:
```
message: |-
  <p style="color: red">
    html
  </p>
```
转为Python如下:
```
{'message': '<p style="color: red">\n  html\n</p>'}
```

#### 七、引用
锚点&和别名*，可以用来引用,&用来建立锚点（defaults），<<表示合并到当前数据，*用来引用锚点
```
defaults: &defaults
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  <<: *defaults

test:
  database: myapp_test
  <<: *defaults
```
等同于下面的代码:
```
defaults:
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  adapter:  postgres
  host:     localhost

test:
  database: myapp_test
  adapter:  postgres
  host:     localhost
```