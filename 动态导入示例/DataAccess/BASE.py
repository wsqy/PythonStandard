# coding:utf-8
from abc import ABCMeta, abstractmethod


class Base(object):
    __metaclass__ = ABCMeta

    def __init__(self, configuration):
        self.config = configuration

    @abstractmethod
    def get_task(self, key):
         pass

    @abstractmethod
    def push_task(self, key, data):
        pass
