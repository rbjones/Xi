==================================
**Introduction to The Xi Project**
==================================

The **Xi** project is a trial in the application
of "Deep Learning" to interactive proof, and a number of other ideas/

To give maximum scope for adaptation of interative
proof to the exploitation of "deep learning" the project
uses a completely new ITP (Interactive Theorem Prover) system,
which implement a new language and logic in novel ways.
The name Xi is used for the project, the language and logic, and for the
interactive theorem prover.
Because this logical system is speculative and will probably prove
to be either inconsistent or unusable, I am thinking of doing a better
established logic as well, HOL (Higher Order Logic), so I will be working
on two interactive proof tools, hopefully sharing a lot of code.

In describing the new logical system and its proof support I may
contrast it with HOL and its proof tools, so it will be easier to
understand what I am saying if you have previous exposure to interactive
proof in HOL.

The main aim is to try out the application of deep learning to ITP, so the
other new things I am thinking of doing with this project are secondary,
and any of them that seems to be getting in the way of the deep learning
I may decide to drop (including the Xi logic).
There's no particular reason why any of them *should* get in the way, but
any of them might prove to be more difficult than I imagine
and in that way might get in the way of my primary purposes,
in which case it may get dropped.

The rest of the introduction falls into three parts.
First a sketch of the generic aspects of the project, those features which
the proof tools share, and then one part each for the specifics of the two
logical systems.

Shared features of the proof tools
..................................

-  A distributed theory datatabase

   All work takes place in a context.
   A context may be associated with a URI and used as a base for further development,
   either by itself or after merging with other contexts.
   Usually the URI will be a URL and the context can be loaded from that URL,
   which would also involve retrieving the contexts in which that context was defined.
   A context, like a HOL theory, provides (in effect) both definitions and theorems.

   Integrity is supported through the use of digital signatures on contexts,
   signed by the authority (man or machine) which is responsible for its creation.
   This ensures that if the context provided by a URI/URL is changed,
   this change can be detected and all results derived in contexts based on it
   can be seen to be unsound.
   Normally modification of a context would be reflected by a change to the URI
   which typically would include a version number.
   
-  Theorem proving will be *distributed*.

   This follows from the distributed nature of the Xi contexts.

-  The implementation language will be python.

   At least that's my starting position, which is mainly because python
   interfaces for Deep Learning seem to be pretty good.
   But if it turns out to be particularly unsuitable for the other aspects
   of the projet I might change my mind!
   (I am new to Phython}

   Tactical programming will use the executable (and compilable)
   subset of the subset of python which provides the elementary
   concrete syntax for Xi.

    
The HOL Logic and its proof tool
................................
   


The Xi Logic and its proof tool
...............................

-  The abstract language and logic Xi

   This is an un-typed illative lambda calculus,
   intended for use with varied concrete syntax
   and in that way providing linguistic pluralism by semantic embedding.

   The most elementary concrete syntax is a functional sublanguage of Python.
   
-  The logic will be a Hilbert style deductive system.

   The deductive system is based on contextual rewriting.
   This means that any subterm can be rewritten using equations derived in the
   process of descending through the term to that subterm.
   The entire context (i.e. in HOL terms, a complete theory hierarchy) in which
   a term is placed, is available for rewriting in that way.

   Though this may appear to the user as if he were doing a "backward" or
   goal oriented proof, this is achieved entirely through forward inference
   by contextual rewriting.
   Thus, a proof of some conjecture A is obtained by rewriting the theorem T
   to A ⇒ A then rewriting the left hand A to T, and finally rewriting
   T ⇒ A to A.

   The flavour is therefore that of proving a conjecture by evaluating it
   and showing that its value is T, and this is further supported by
   allowing effectively computable functions to be compiled and for the
   execution of this compiled code to contribute to the proof (or evaluation)
   of conjectures directly or indirectly involving that function.

-  The implementation paradigm will be derived from the LCF paradigm.
   Not sure how much of that paradigm will remain after the changes
   I have in mind.
