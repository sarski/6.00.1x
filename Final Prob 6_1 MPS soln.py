# -*- coding: utf-8 -*-
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if not atMe:
       return newFrob
    
    i = atMe
    while i.getBefore() != None:
        i = i.getBefore()
        
    while i.myName() < newFrob.myName() and i.getAfter():
        i = i.getAfter()
    if i.myName() >= newFrob.myName():
        if i.getBefore():
            i.getBefore().setAfter(newFrob)
            newFrob.setBefore(i.getBefore())
        newFrob.setAfter(i)
        i.setBefore(newFrob)
    else:
        i.setAfter(newFrob)
        newFrob.setBefore(i)
