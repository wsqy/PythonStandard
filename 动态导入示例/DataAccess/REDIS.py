# coding:utf-8
from BASE import Base


class Redis(Base):
    def __init__(self):
        pass

    def get_task(self, key):
        print("REDIS")

    def push_task(self, key, data):
        pass
