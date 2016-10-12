#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    =====================
    The Xi(Ξ) Term Module
    =====================

    :copyright: Copyright 2016 Roger Bishop Jones
    :license: BSD 2-Clause Licence, see LICENCE for details.

    I did consider making this into a class, but I couldn't figure
    out what the benefit would be, so for the time being its just
    a module defining various functions for making taking apart and
    otherwise processing terms.

    The terms are represented by triples.
    The first element is a number which tells you whether the term
    a variable, an abstraction or an application.

    In a variable the second element of the tuple is its name and the
    third is zero

    In an abstraction the second element is the name of the variable
    being bound and the third is the body of the abstraction (a term).

    In an application the second and third elements of the tuple are
    the function and the argument (both terms).
"""

def MkVar (name:str):
    """ construct a term which is a variable 

    >>> MkVar("Ξ")
    (0, 'Ξ', 0)
    """
    return (0, name, 0)

def MkAbs (v:str, b):
    """ constructs a term which is an abstraction 

    >>> MkAbs("∀", MkVar("Ξ"))
    (1, '∀', (0, 'Ξ', 0))
    """
    return (1, v, b)

def MkApp (f, a):
    """ constructs a term which is an application

    >>> MkApp(MkVar("∀"), MkVar("Ξ"))
    (2, (0, '∀', 0), (0, 'Ξ', 0))
    """
    return(2, f, a)

def IsVar (t):
    """ tests whether a term is a variable

    >>> IsVar(MkApp(MkVar("∀"), MkVar("Ξ")))
    False
    >>> IsVar(MkVar("Ξ"))
    True
    """
    return t[0] == 0

def IsAbs (t):
    """ tests whether a term is an abstraction

    >>> IsAbs(MkAbs("∀", MkVar("Ξ")))
    True
    >>> IsAbs(MkVar("Ξ"))
    False
    """
    return t[0] == 1

def IsApp (t):
    """ tests whether a term is an application

    >>> IsApp(MkApp(MkVar("∀"), MkVar("Ξ")))
    True
    >>> IsApp(MkVar("Ξ"))
    False
    """
    return t[0] == 2

def DestTerm (t):
    """ disassembles a term, returning a 3-tuple in which the first element
        is 0, 1 or 2 according as the term is a variable,
        abstraction or application, and the next one or two elements are
        the immediate constituents.

    >>> DestTerm(MkApp(MkVar("∀"), MkVar("Ξ")))
    (2, (0, '\u2200', 0), (0, '\u039e', 0))
    >>> DestTerm(MkVar("Ξ"))
    (0, '\u039e', 0)
    """
    return t

def Frees (t):
    """ returns the set of free variables of a term

    >>> Frees(MkApp(MkVar("∀"), MkVar("Ξ")))
    {'Ξ', '∀'}
    >>> Frees(MkVar("Ξ"))
    {'Ξ'}
    >>> Frees(MkAbs("∀", MkVar("Ξ")))
    {'Ξ'}
    >>> Frees(MkAbs("Ξ", MkVar("Ξ")))
    set()
    """
    k = t[0]
    if k == 0: return set(t[1])
    elif k == 1: return Frees(t[2]) - set(t[1])
    elif k == 2: return Frees(t[1]) | Frees(t[2])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
