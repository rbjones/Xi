# Xi
An experimental approach to deep learning interactive theorem proving.

This is primarily for me an educational exercise in the application of Deep Learning to Interactive Theorem Proving.

I have some experience with interactive theorem proving, both in the use and the development of these tools, mainly through my involvement in the development and application of ProofPower, but I have no practical experience of neural nets.

I have decided to do this through the development of an entirely new interactive theorem prover, using a language I have never used before (python).

In the course of developing an ITP for industrial applications many compromises are necessary, and so there are many ideas which I have favoured but not been able to do (mostly because of needing to be risk averse).
This experiment will evaluate many of these ideas, so its a bit like a fantasy ITP, to many speculative ideas to have much chance of success.
Its here on a public repository not so much in the expectation of collaborative participation as just in case one or more of the ideas might prove useful to someone else.

In the rest of this README I will outline the novel features which I hope to explore with this prototype.

The name of the project, "Xi" is the name of a greek letter, &Xi;, which has some history in Combinatory logic.
It was used by Haskell B. Curry and his collaborators for the illative combinator known as "restricted generality".
It will also be used in the logic supported by the proposed interactive proof tool, though it will in this case be used as an illative combinator in an illative lambda-calculus for equality if terms.

**Xi** is the name of the project and of the language it supports.
The proposed logic is called "XiL" and the interactive prover "XiP", sometimes rendered "&Xi;L" and "&Xi;P" (though I don't propose to use &Xi; as an alternative to "Xi" for the project name, so "&Xi;" by itself refers to the language.).

The proposed logic is itself highly speculative.
It is not yet defined and there is a high risk that (like most supposedly strong illative combinatory logics) it will prove inconsistent.
In the short term it will benefit only from an informal rationale.

The remainder of the README will enumerate with the briefest of explanations the key features of the system proposed.

1. It will support the abstract logic &XiL;, which has no definite concrete syntax.  Other languages and logics as concrete presentations of &Xi;L expressions.

2. The logic will be a Hilbert style deductive system.

3. The implementqtion paradigm will be derived from the LCF paradigm.

4. The implementation language will be python, but an executable subset of &Xi; will be used for tactical programming.

5. Theorem proving will be *distributed*.
