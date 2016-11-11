# coding:utf-8
from BASE import Base


class Memcache(Base):
    def __init__(self):
        pass

    def get(self, key):
        print("Memcache")
