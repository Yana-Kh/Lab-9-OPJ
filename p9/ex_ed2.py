#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    my_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }
    new_dict = {numb: s for s, numb in my_dict.items()}
    print("Исходный словарь")
    print(my_dict)
    print("Обратный словарь")
    print(new_dict)


