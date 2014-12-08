#!/usr/bin/python

from pyswip import *
import sys


def bar(t):
    print"FooBar,", t
bar.arity = 1

def barfoo(t):
    print"FooBar,", t
bar.arity = 1

foo = Functor("foo", 1)
def main():
    prolog = Prolog()
    prolog.consult("test.pl")
    registerForeign(bar)
    call(foo("X"))

main()
