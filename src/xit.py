#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    =====================
    The Xi(Ξ) Term Module
    =====================

    :copyright: Copyright 2016 Roger Bishop Jones
    :license: BSD 2-Clause Licence, see LICENSE for details.

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

def MkVar (name):
    """ construct a term which is a variable """
    return (0, name, 0)

def MkAbs (v, b):
    """ constructs a term which is an abstraction """
    return (1, v, b)

def MkApp (f, a):
    """ constructs a term which is an application """
    return(2, f, a)

def IsVar (k, l, r):
    """ tests whether a term is a variable """
    return k == 0

def IsAbs (k, l, r):
    """ tests whether a term is an abstraction """
    return k == 1

def IsApp (k, l, r):
    """ tests whether a term is an application """
    return k == 2

def DestTerm (k, l, r):
    """ disassembles a term, returning a 3-tuple in which the first element
        is 0, 1 or 2 according as the term is a variable,
        abstraction or application, and the next one or two elements are
        the immediate constituents."""
    return (k, l, r)


