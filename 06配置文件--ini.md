python2--->ConfigParser 
python3 -->configparser
��������ûʲô�仯�������и������Ե�д���ǣ�
```
try:
    import ConfigParser
except:
    import configparser as ConfigParser
```
��ʼ���࣬�����������ļ�
```
conf = ConfigParser.ConfigParser()
conf.read("settings.ini")
```
��ȡ�����ļ������е� sections������
```
sectctions = conf.sections()
```
���ؽ���ǣ�
```
['sec_a', 'sec_b']

```
��ȡָ��sections�����е�options:
```
options = conf.options("sec_b")
```
���ؽ��:
```
['b_key1', 'b_key2', 'b_key3', 'b_key4']

```
�õ�ָ��section�����м�ֵ��
```
kvs = conf.items("sec_b")
```
���ؽ��:
```
[('b_key1', '121'), ('b_key2', 'b_value2'), ('b_key3', '$r'), ('b_key4', '127.0.0.1')]
```

�õ�ָ��section,option��ֵ
```
str_vaule = conf.get("sec_b", 'b_key2')
print(str_vaule)
print(type(str_vaule))
```
���ؽ��:
```
b_value2
<type 'str'>
```
- get�������ַ�ʽ        
  - getint--��ȡ����ֵ
  - getfloat--��ȡ������
  - getboolean--��ȡbool����

- ini�ļ���ʹ�ñ��� �� %(ʹ�õı���)s

-------------------
ini�ļ�ʹ������
iniû���������飬Ҫʹ���������ڶ����ʱ���Զ��ŷָ�,����ʱʹ��python�ַ�����spilt�������ָ������
such:
�����ļ���
```
# settings.ini
[sec_a]
a_key1 = qu,yuan,ququu
```
������
```
str_vaule = conf.get("sec_a", 'a_key1').split(",")
print(str_vaule)
```
���:
```
['qu', 'yuan', 'ququu']
```

------------
ini�ļ�ʹ���ֵ�
iniʹ���ֵ䣬����һ��sections���ֵ�ļ�ֵ�������涨��
such:
�����ļ���
```
# settings.ini
[db]
host = 127.0.0.1
port:3306
dbname:qy
```
������
```
db = dict(conf.items("db"))
print(db)
```
���:
```
{'host': '127.0.0.1', 'port': '3306', 'dbname': 'qy'}
```

