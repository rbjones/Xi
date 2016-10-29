============
The Logic Xi
============

I am considering two deductive systems for this project.
One is the well established HOL logic, a polymorphic form of Church's
Simple Type Theory as implemented in the Cambridge HOL system, and in
HOL light, ProofPower and other systems.

The second is the Logic which I am calling Xi or Ξ, of which the rest of
this document is a sketch.

The system will have a dual presentation.
In the more primitive of these presentations it is a type-free,
"illative" lambda calculus
(i.e. a lambda calculus with a primitive logical combinator).
The primitive combinator is an approximation to equality of the terms
of the language, and is a partial equivalence relation.
In this form the deductive system is a Hilbery-style deductive system
in which the sentences are terms of the illative lambda calculus, and
the deductive system proves a subset of the terms reducible to "T".
A distinctive feature of this lambda-calculus is that there is no
distinction between variables and constants, so in this way it is
similar to most programming languages.

Under this interpretation, the entire theory heirarchy is construed as
a lambda-term with the proof process adding additional subterms as
required.

In practice the principle mode of inference is by contextual rewriting of terms,
i.e. by the rewriting of subterms using equations which are derivable from
the context of the subterm in the term as a whole.
This is best described by giving the structure of a "context" in which the
context of subterm is captured for use in transforming the subterm, and the
theory hierarchy is then viewed as providing the top or earliest layers of
the structured context for the theorems being derived.

The following details are very tentative, particularly the concrete syntax,
which will in any case be varied according to context.

The inference rules are:

    alpha-conversion

    beta-conversion
  
    there is just one primitive combinator which I had intended to call Xi(Ξ) and approximates
    equality, but maybe better just to use "=".
    
    Using "=" we define and axiomatise as follows:

    T = λx y.x
    
    F = λx y.y

    Now think of a (partial) set as a function which yields T when
    and only when applied to members of the set.
    On this basis we now define a very important notion of
    universal quantification.

    The universal here is bounded quantification or what the combinatory
    theorists called restricted generality (and used the symbol Ξ for):
    
    ∀ = λp q. (p = λx.(p x)(q x)(p x))

    Think of the first argument as a set and the second as a predicate which is true
    for every member of that set.

    I will use the sugar ∀x:A.B to mean ∀A(λx.B)

    You can get unrestricted universal quantification by defining V as:

    V = λx.T

    So universal quantification can be written "∀x:V.A(x)".
    We won't be using it a lot, because not much is true of everything.

    ∀ = λp. (p = λx.T)
    
    ∀x. x = x
    
    ¬ = λx y z. x z y
    
    ≠ = λx y. ¬(x = y)
    
    T ≠ F

    ∨ = λx y. x T y
    
    ∧ = λx y. x y F

    ⇒ = λx y. y ∨ ¬ x

    ∀ f g x. f x ≠ g x ⇒ f ≠ g
   
    Substitution into subterms using equations in the context of the term.
    This is a rule stating that if an equation is derivable in some context
    then a term in that context can be rewritten using that equation.
    
    C ⇒ X=Y,  C ⇒ T
    
    \===============
    
    C ⇒ T[Y/X]

    Where T[Y/X] is the result of substituting Y for X in T,
    provided X is free for Y in T.
    
    Strength is given by two axioms, the exact form not yet settled.
    and the consistency of which are controversial:

    - choice, in the form a well-ordering assertion

    - strong infinity, asserting the existence of a large well-ordering
    
    
