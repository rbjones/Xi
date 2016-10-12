#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    =====================
    The Xi(Ξ) Term Module
    =====================

    :copyright: Copyright 2016 Roger Bishop Jones
    :license: BSD 2-Clause Licence, see LICENCE for details.

    In this module the class of terms is defined.
"""

Class XiTerm:
    """The Class of Terms of the language Xi,
    essentially a type-free lambda calculus.

    The terms are represented by triples.
    The first element is a number which tells you whether the term
    a variable, an abstraction or an application.

    In a variable the second element of the tuple is its name and the
    third is zero

    In an abstraction the second element is the name of the variable
    being bound and the third is the body of the abstraction (a term).

    In an application the second and third elements of the tuple are
    the function and the argument (both terms).""

def __init__ (self, k, n, lterm, rterm)
    """an XiTerm consists of a 4-tuple as follows:
    1. the kind of term (0=variable, 1=abstraction, 2=application)
    2. the name (a string, empty for applications)
    3. the body of the abstraction, or the function of an application
    4. the argument of an abstraction (self unless an application)"""

    self.kind = k
    self.name = n
    self.left = lterm
    self.right = rterm

def MkVar (name:str):
    """ construct a term which is a variable """
    return (0, name, 0)

def MkAbs (v, b):
    """ constructs a term which is an abstraction """
    return (1, v, b)

def MkApp (f, a):
    """ constructs a term which is an application """
    return(2, f, a)

def IsVar (t):
    """ tests whether a term is a variable """
    return t(0) == 0

def IsAbs (t):
    """ tests whether a term is an abstraction """
    return t(1) == 1

def IsApp (t):
    """ tests whether a term is an application """
    return t(2) == 2

def DestTerm (t):
    """ disassembles a term, returning a 3-tuple in which the first element
        is 0, 1 or 2 according as the term is a variable,
        abstraction or application, and the next one or two elements are
        the immediate constituents."""
    return t

def Frees (k, l, r):
    """ returns the set of free variables of a term """
    k = t(0)
    if k == 0: return set(l)
    elif k == 1: return Frees(t(2)) - set(t(1))
    elif k == 2: return Frees(t(1)) & Frees(t(2))
