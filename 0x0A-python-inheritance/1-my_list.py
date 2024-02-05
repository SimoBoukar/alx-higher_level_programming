#!/usr/bin/python3
'''MyList class.'''


class MyList(list):
    '''MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))
