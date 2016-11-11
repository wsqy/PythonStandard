# coding:utf-8
from __future__ import print_function
import json


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person Object name : %s , age : %d' % (self.name, self.age)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        # convert object to a dict
        d = {}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict2object)

    def dict2object(self, d):
        # convert dict to object
        if'__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            # get args
            args = dict((key.encode('ascii'), value) for key, value in d.items())
            # create new instance
            inst = class_(**args)
        else:
            inst = d
        return inst

if __name__ == '__main__':
    person = Person('Peter', 22)
    d = MyEncoder().encode(person)
    print(d)
    print("---------------")
    o = MyDecoder().decode(d)
    print(o)
