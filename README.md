# LISP Processor

This is a first attempt at writing an interpreter for a subset of Racket. Racket is a LISP (hence the project name), and a dialect of Scheme. The goal is to implement the core LISP features, with some of these special language features being stretch goals:

- Exact numbers
- Vectors
- Structs
- Modules

I would also like to make an option to use Typed Racket.

## Sources

The documentation for the Racket language can be found at [docs.racket-lang.org](https://docs.racket-lang.org/). Of particular help is the [Racket Reference](https://docs.racket-lang.org/reference/index.html).

I'm borrowing a lot from the book _Writing Compilers and Interpreters: A Modern Software Engineering Approach Using Java, Third Edition_, by Ronald Mak. The difference being that the book implements a compiler and interpreter for Pascal in Java, while this project implements an interpreter for Racket in Python.


