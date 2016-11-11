
�ο�[��һ���YAML ���Խ̳�](http://www.ruanyifeng.com/blog/2016/07/yaml.html?f=tt),������javascתΪ�˵�pythonʵ��

#### һ�����

YAML ���ԣ����� /?j?m?l/ �������Ŀ�꣬���Ƿ��������д����ʵ������һ��ͨ�õ����ݴ��л���ʽ��

���Ļ����﷨��������:
- ��Сд����
- ʹ��������ʾ�㼶��ϵ
- ����ʱ������ʹ��Tab����ֻ����ʹ�ÿո�
- �����Ŀո���Ŀ����Ҫ��ֻҪ��ͬ�㼶��Ԫ�������뼴��  

\# ��ʾע�ͣ�������ַ�һֱ����β�����ᱻ���������ԡ�

YAML ֧�ֵ����ݽṹ������:
- ���󣺼�ֵ�Եļ��ϣ��ֳ�Ϊӳ�䣨mapping��/ ��ϣ��hashes�� / �ֵ䣨dictionary��
- ���飺һ�鰴�������е�ֵ���ֳ�Ϊ���У�sequence�� / �б�list��
- ������scalars���������ġ������ٷֵ�ֵ

#### ��������
�����һ���ֵ�ԣ�ʹ��ð�Žṹ��ʾ:
```
animal: pets
```
תΪPython����:
```
{'animal': 'pets'}
```
Yaml Ҳ������һ��д���������м�ֵ��д��һ�����ڶ���
```
hash: { name: Steve, foo: bar } 
```
תΪPython����:
```
{'hash': {'foo': 'bar', 'name': 'Steve'}}
```

#### ��������
һ�������߿�ͷ���У�����һ������:
```
- Cat
- Dog
- Goldfish
```
תΪPython����:
```
['Cat', 'Dog', 'Goldfish']
```
���ݽṹ���ӳ�Ա��һ�����飬������ڸ�����������һ���ո�:
```
-
 - Cat
 - Dog
 - Goldfish
```
תΪPython����:
```
[['Cat', 'Dog', 'Goldfish']]
```
����Ҳ���Բ������ڱ�ʾ��:
```
animal: [Cat, Dog]
```
Ҳ��������������д����
```
animal:
  - Cat
  - Dog

```
תΪPython����:
```
{'animal': ['Cat', 'Dog']}
```

##### �ġ����Ͻṹ
�����������Խ��ʹ�ã��γɸ��Ͻṹ:
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
תΪPython����:
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

#### �塢���� 

yamlд�� | python�������� | ˵��
---|---|---
`number: 12.30` | `{'languages': 12.1}` |  ��ֱֵ��������������ʽ��ʾ
`isSet: true` | `{'isSet': True}` |  ����ֵ��`true`��`false`��ʾ
`parent: ~ ` | `{'parent': None}` |  `null`��`~`��ʾ
`iso8601: 2001-12-14t21:59:43.10-05:00 ` | `{'iso8601': datetime.datetime(2001, 12, 15, 2, 59, 43, 100000)}` | ʱ����� `ISO8601` ��ʽ
`date: 1976-07-31` | `{'date': datetime.date(1976, 7, 31)}` | ���ڲ��ø��� iso8601 ��ʽ���ꡢ�¡��ձ�ʾ
`e: !!str 123` | {'e': '123'} | YAML ����ʹ��������̾�ţ�ǿ��ת����������


#### �����ַ���
�ַ����������Ҳ����ӵ�һ���������ͣ��ַ���Ĭ�ϲ�ʹ�����ű�ʾ��
```
str: string
```
תΪPython����:
```
{'str': 'string'}
```

����ַ���֮�а����ո�������ַ�����Ҫ��������֮��(ò�Ʋ�������Ҳû���⣬����������ô˵�ˣ��ͼ��°�):
```
str: This is string
```
תΪPython����:
```
{'str': 'This is string'}
{'str': 'This is string'}
```
�����ź�˫���Ŷ�����ʹ�ã�����==˫���Ų���������ַ�ת��==
```
s1: 'context\nstring'
s2: "context\nstring"
```
תΪPython����:
```
{
    's1': 'context\\nstring',
    's2': 'context\nstring',
}
```
������֮��������е����ţ���������ʹ������������ת��:
```
str: 'labor''s day' 
# ����Ҳ�� str: "labor's day"
```

תΪPython����:
```
{'str': "labor's day"}
```
�ַ�������д�ɶ��У��ӵڶ��п�ʼ��������һ�����ո����������з��ᱻתΪ�ո�
```
str: str1
  str2
  str3
```
תΪPython����:
```
{'str': 'str1 str2 str3'}
```


�����ַ�������ʹ��`|`�������з���Ҳ����ʹ��`>`�۵�����(��β����ʾһ�����У�������ʾ�ɿո�):
```
this: |
  Foo
  Bar
that: >
  Foo
  Bar
```
תΪPython����:
```
{'this': 'Foo\nBar\n', 'that': 'Foo Bar\n'}
```
`+`��ʾ�������ֿ�ĩβ�Ļ��У�`-`��ʾɾ���ַ���ĩβ�Ļ��У�
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
תΪPython����(Ϊ���Ķ���˳�����ҽ���ʽ������һ��):
```
{
  's1': 'Foo\n',
  's2': 'Foo\n',
  's3': 'Foo\n\n\n',
  's4': 'Foo'
}
```
�ַ���֮�п��Բ��� `HTML` ���:
```
message: |-
  <p style="color: red">
    html
  </p>
```
תΪPython����:
```
{'message': '<p style="color: red">\n  html\n</p>'}
```

#### �ߡ�����
ê��&�ͱ���*��������������,&��������ê�㣨defaults����<<��ʾ�ϲ�����ǰ���ݣ�*��������ê��
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
��ͬ������Ĵ���:
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