#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:24:17 2020

@author: kash-py
"""




def move_left(tpl):
    return (tpl[0] -1,tpl[1])


def move_right(tpl):
    return (tpl[0] +1,tpl[1])

def move_down(tpl):
    return (tpl[0], tpl[1] - 1)

def move_up(tpl):
    return (tpl[0], tpl[1] + 1)


def apply(Oplist, arg_tuple):
    if len(Oplist) == 0:
        return arg_tuple
    else:
        return apply(Oplist[1:],Oplist[0](arg_tuple))
    
print(apply([move_left, move_right, move_down, move_up],(2,5)))


def addLevel(Oplist, operations):
    return [x +[y] for y in operations for x in Oplist]


cannot_be_nums = (0,6) # matrix is not that big

#print(move_left((1,5)))
#print(move_right((1,5)))
#print(move_down((1,5)))
#print(move_up((1,5)))


initial_tuple = (1,6)
goal_tuple = (6,1)

def findSequence(initial, goal):
    opList = [[]]
    for i in range(19):
        #print(i)
        opList = addLevel(opList, [move_left, move_right, move_down, move_up])
        #print(opList)
        for seq in opList:
            #print(seq)
            if apply(seq, initial) == goal:
                return seq
    
    
    
    

print(findSequence(initial_tuple, goal_tuple))
    


