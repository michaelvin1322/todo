# -*- coding: utf-8 -*-

from utils import get_input_function


class Storage(object):  # storage = Storage() # This Class creates list of todo items
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):  # this class creates the base for any todo item
    def __init__(self, heading):
        self.heading = heading
        self.done = False

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):  # this class is simplest todo item. It has only one attribute.
    def __str__(self):
        return 'ToDo: {}'.format(
            self.heading
        )

    @classmethod
    def construct(cls):  # this method fill attribute. It creates todo item
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToBuyItem(BaseItem):  # this class is tobuy item.
    def __init__(self, heading, price):  # now we create attributes
        super(ToBuyItem, self).__init__(heading)
        self.price = price

    def __str__(self):
        return 'ToBuy: {} for {}'.format(
            self.heading,
            self.price,
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)


class ToReadItem(BaseItem):
    def __init__(self, heading, url):
        super(ToReadItem, self).__init__(heading)
        self.url = url

    def __str__(self):
        return 'ToRead: {} in {}'.format(
            self.heading,
            self.url,
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        url = input_function('Input link: ')
        return ToReadItem(heading, url)

