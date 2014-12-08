#!/usr/bin/python

from pyswip import *
import sys


running = 1

def end():
    print"Bye,"
    global running
    running = 0
end.arity = 0


def help():
    print"Print a cool help screen"
help.arity = 0



def moveTo(obj):
    print "moving to", obj
moveTo.arity = 1

def addReg(k):
    registerForeign(k)
    #k.arity = 1



addReg(help)
addReg(moveTo)



sentence = Functor("sentence", 1)
execute = Functor("execute_cmd",1) 
command = Functor("command",2) 
#call = Functor("call",1) 

def main():
    prolog = Prolog()
    prolog.consult("nl-facts.pl")
    registerForeign(end)
    global running
    while running:
        line = raw_input("> ")
        l = line.split()
        print l.__str__()
        call(execute(l))
main()
