##### [JSOn�����Լ�PYTHON��JSON����ز���](http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html)  
JSON��һ�������������ݽ�����ʽ���������Ķ��ͱ�д��ͬʱҲ���ڻ����Ľ��������ɣ�JSON������ȫ���������Ե��ı���ʽ������Ҳʹ����������C���Լ����ϰ�ߡ�
JSON���������ֽṹ:
- "��ֵ��"�ļ��ϣ��ڲ�ͬ���������Ϊ����(object), ��¼(record), �ṹ(struct), �ֵ�(dictionary), ��ϣ��(hash table, �м��б�(keyed list), ���߹�������(associative array)
- ֵ�������б�(A ordered list of vaules) ,�ڴ󲿷������У��������Ϊ����(array)

[json�ٷ�˵��](http://json.org/)

[Python����json�ı�׼api��ο�](http://docs.python.org/library/json.html)

++ע����2.6�����°汾�У�jsonģ��Ϊsimplejson,Ϊ�˼��ݣ�����jsonģ���ʱ�������µķ�ʽ����,Ϊ�˷��㣬�ڴ��ĵ�����ʹ��import json������������ε���++
```
try:
    import json
except ImportError:
    import simplejson as json
```
#### �Լ��������͵�encoding �� decoding��
- ʹ�ü򵥵�json.dumps�����Լ��������ͽ��б��룬���磺  
    ����:
    ```
    import json
    obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
    encodedjson = json.dumps(obj)
    print(obj)
    print(encodedjson)
    ```
    ���:
    ```
    [[1, 2, 3], 123, 123.123, 'abc', {'key2': (4, 5, 6), 'key1': (1, 2, 3)}]
    [[1, 2, 3], 123, 123.123, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]
    ```
    ͨ������Աȿ��Կ��� ������ͨ��encode֮����ԭʼ���������ͷǳ����Ƶ��ǻ�����Щ�������ͷ����˸ı��,����Ԫ�������б���json��������У�����ڴ�pythonԭʼ������json����ת���Ĺ���,�����ת����������: 
    PYTHON | JSON
    --- | ---
    dict | object
    list, tuple | array
    str, unicode | array
    int, long(python3��), float | number
    True, False | true, false
    None | null

- json.dumps()����������һ��str�����encodejson, ���ǽ�������encodejson����decode,�õ�ԭʼ���ݣ���Ҫʹ��json.loads()����
    ```
    import json
    decodejson = json.loads(encodedjson)
    print(type(decodejson))
    print(decodejson)
    ```
    �������:
    ```
    <class 'list'>
    [[1, 2, 3], 123, 123.123, u'abc', {u'key2': [4, 5, 6], u'key1': [1, 2, 3]}] py2.7
    [[1, 2, 3], 123, 123.123, 'abc', {'key2': [4, 5, 6], 'key1': [1, 2, 3]}]  #py3.x
    ```
    loads����������ԭʼ�Ķ��󣬵�����Ȼ������һЩ�������͵�ת�������磬�����С�abc��ת��Ϊ��unicode���͡���json��python������ת���������£�
    JSON | Python
    --- | ---
    object | dict
    array | list
    string | unicode(python2)|str(python3)
    number(int) | int,long(python3��)
    number(real) | float
    true|false | True|False
    null | None
    
- json.dumps�����ṩ�˺ܶ���õĲ����ɹ�ѡ�񣬱Ƚϳ��õ���sort_keys����dict���������������֪��Ĭ��dict�������ŵģ���separators��indent�Ȳ�����
    - ������ʹ�ô洢�����ݸ��������ڹ۲죬Ҳʹ�ö�json����Ķ�����бȽϣ����磺
        ```
        data1 = {'b':789,'c':456,'a':123}
        data2 = {'a':123,'b':789,'c':456}
        d1 = json.dumps(data1,sort_keys=True)
        d2 = json.dumps(data2)
        d3 = json.dumps(data2,sort_keys=True)
        print(d1)
        print(d2)
        print(d3)
        print(d1 == d2)
        print(d1 == d3)
        ```
        ���������
        ```
        {"a": 123, "b": 789, "c": 456}
        {"a": 123, "c": 456, "b": 789}
        {"a": 123, "b": 789, "c": 456}
        False
        True
        ```
        �����У�����data1��data2����Ӧ����һ���ģ���������dict�洢���������ԣ���������޷��Ƚϡ�������߿���ͨ�������Ľ�����д洢�ͱ��������ݱȽϲ�һ�µ��������������������ٽ��д洢��ϵͳ�ض�Ҫ����һЩ���飬Ҳһ����������һ�����������ģ������ʵ������Ǻ���Ҫ�ġ�
    - indent��������������˼��������ʹ�����ݴ洢�ĸ�ʽ��ø�������
        ```
        data1 = {'b':789,'c':456,'a':123}
        d1 = json.dumps(data1,sort_keys=True,indent=4)
        print(d1)
        ```
        �������:
        ```
        {
            "a": 123,
            "b": 789,
            "c": 456
        }
        ```
        ��������ݱ���ʽ��֮�󣬱�ÿɶ��Ը�ǿ������ȴ��ͨ������һЩ����Ŀհ׸����������ġ�json��Ҫ����Ϊһ������ͨ�ŵĸ�ʽ���ڵģ�������ͨ���Ǻ��ں����ݵĴ�С�ģ����õĿո��ռ�ݺܶ�ͨ�Ŵ��������ʵ�ʱ��ҲҪ�����ݽ���ѹ��
    
    - separator�������������������ã��ò���������һ��Ԫ�飬�����ָ������ַ���
        ```
        data = {'b': 789, 'c': 456, 'a': 123}
        print('repr(DATA)             :', repr(data))
        print('len(repr(data))        :', len(repr(data)))
        print('dumps(data)            :', len(json.dumps(data)))
        print('dumps(data, indent=2)  :', len(json.dumps(data, indent=2)))
        print('dumps(data, separators):', len(json.dumps(data, separators=(',',':'))))
        print("-------------------------")
        print('dumps(data)            :', json.dumps(data))
        print('dumps(data, separators):', json.dumps(data, separators=(',',':')))
        ```
        ��������:
        ```
        ('repr(DATA)             :', "{'a': 123, 'c': 456, 'b': 789}")
        ('len(repr(data))        :', 30)
        ('dumps(data)            :', 30)
        ('dumps(data, indent=4)  :', 46)
        ('dumps(data, separators):', 25)
        -------------------------
        ('dumps(data)            :', '{"a": 123, "c": 456, "b": 789}')
        ('dumps(data, indent=4)  :', '{\n    "a": 123, \n    "c": 456, \n    "b": 789\n}')
        ('dumps(data, separators):', '{"a":123,"c":456,"b":789}')
        ```
        ͨ���Ƴ�����Ŀհ׷����ﵽ��ѹ�����ݵ�Ŀ�ģ�����Ч�����ǱȽ����Եġ�
    - ��һ���Ƚ����õ�dumps������skipkeys��Ĭ��ΪFalse�� dumps�����洢dict����ʱ��key������str���ͣ�����������������͵Ļ�����ô�����TypeError�쳣����������ò�������ΪTrue�Ļ������Ƚ����ŵĹ���(���Ÿ���ֱ�ӰѲ���������)��
        ```
        data = {'b':789,'c':456,(1,2):123}
        print(json.dumps(data,skipkeys=True))
        ```
        ���������
        ```
        {"c": 456, "b": 789}
        ```
------------------------------------------------------------------
�������json�������ļ�
```
# settings.json
{
    "db":{
        "ip":"127.0.0.1",
        "port":3306
    },
    "web":{
        "ip":"127.0.0.1",
        "port":80
    }

}
```
���������ļ�:
```
#cat k.py
def jx_json(fls):
    print('��ã�')
    with open(fls, 'r') as jsf:
        res = json.load(jsf)
        print(res['db']['ip'])
        print(res['db']['port'])

if __name__ == "__main__":
    jx_json(fls="settings.json")
```
