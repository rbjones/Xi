The Logic XiL
_____________

The deductive system is as yet not settled, but will likely be a Hilbert style forward inference system in which theorems are just terms of the language (though with elaborate presentations) and inference by contextual rewriting of subterms.

The following details are very tentative.

The inference rules are:

    alpha-conversion

    beta-conversion
  
    there is just one primitive combinator which is Xi(Ξ) and approximates equality
    though maybe better just to use "=".
    
    Using "=" we define and axiomatise as follows:

    T = λx y.x
    
    F = λx y.y

    ∀ = λp. p = λx.T
    
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
    ===============
    C ⇒ T[Y/X]

    Where T[Y/X] is the result of substituting Y for X in T,
    provided X is free for Y in T.
    
Strength is given by two axioms, the consistency of which is controversial:

    choice, in the form a well-ordering assertion
        (under which a well-ordering of the universe serves as a set of ordinals)

    strong infinity, asserting at least that the universe is inaccessible
    
