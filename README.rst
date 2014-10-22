coroutine-generation - Combinatorial Generation In Python
#########################################################

A library to show-case use of coroutines for combinatorial generation. The
following combinatorial generation algorithms currently have coroutine-based
implementations in this repository:

- BGRC algorithm for binary strings in Gray order,
- Generalization of BGRC for multi-radix numbers in Gray order,
- Steinhaus-Johnson-Trotter for permutations in Gray order,
- Knuth-Ruskey for ideals of a completely acyclic poset in Gray order (AKA "spider-squishing"),
- Varol-Rotem for linear extensions of a poset,
- Pruesse-Ruskey for signed linear extensions of a poset in Gray order.

More algorithms might be added soon.  There are also several simpler examples,
and alternative (not coroutine-based) implementations provided for comparison.
For much more detail, see the accompanying article at
`http://sahandsaba.com/combinatorial-generation-using-coroutines-in-python.html
<http://sahandsaba.com/combinatorial-generation-using-coroutines-in-python.html>`_.

NOTE: This repository is currently undergoing heavy refactoring and
modification. Some of the algorithms might be half-finished or not fully
tested.

Running Tests
=============
Since the repository is now in package form, you need to run modules using
Python's `-m` parameter, like this:

.. code::

    python3.4 -m combgen.multiradix_gray.tests
