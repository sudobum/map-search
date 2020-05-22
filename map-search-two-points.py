#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:24:17 2020

@author: kash-py
"""




matrix = [[x]+[y] for x in range(1,6) for y in range(1,6) ]
print(matrix.reverse())





def longest_list(list_of_lists):
    return [y for y in list_of_lists if len(y) == max([len(x) for x in list_of_lists])][0]

def shortest_list(list_of_lists):
    return [y for y in list_of_lists if len(y) == min([len(x) for x in list_of_lists])][0]






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
    
#print(apply([move_left, move_right, move_down, move_up],(2,5)))


def addLevel(Oplist, operations):
    return [x +[y] for y in operations for x in Oplist]


cannot_be_nums = (0,6) # matrix is not that big

#print(move_left((1,5)))
#print(move_right((1,5)))
#print(move_down((1,5)))
#print(move_up((1,5)))

"""
given three coordinates which
one should i go to first, second, third

map is a 5x5 matrix

[[1, 5], [2, 5], [3, 5], [4, 5], [5, 5],
 [1, 4], [2, 4], [3, 4], [4, 4], [5, 4],
 [1, 3], [2, 3], [3, 3], [4, 3], [5, 3],
 [1, 2], [2, 2], [3, 2], [4, 2], [5, 2],
 [1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]


starting position 1,5 | list of postions [[3,5],[1,3],[5,2]]

"""
initial = (1,5)
goal = (5,2)

goals = ((3,5),(1,4),(5,4))

def findSequence(initial, goal):
    opList = [[]]
    for i in range(15):
        #print(i)
        opList = addLevel(opList, [move_left, move_right, move_down, move_up])
        #print(opList)
        for seq in opList:
            #print(seq)
            if apply(seq, initial) == goal:
                return (seq)
    
    
    
    




def shortest_way(initials, goal):
    ways = []
    for initial in initials:
        ways.append(findSequence(initial, goal))  
    #print(ways)    
    return shortest_list(ways)    
        
print(shortest_way(goals,goal))    














    


