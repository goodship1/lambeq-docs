.. _sec-manual-training:

Manual training
===============

While the :py:mod:`.training` package is the recommended way of performing supervised learning with ``lambeq``, there might be use cases where more flexibility is needed, for example when someone wants to use an unsupported ML backend. In this tutorial, we show how training can be performed with ``lambeq`` at a lower level.

In general, there are many ways to train a ``lambeq`` model, and the right one to use depends on the task at hand, the type of experiment (quantum or classical), and even other factors, such as hardware requirements. At the highest level, the process involves the following steps (for the classical case):

#. Extract the word :term:`symbols <symbol>` from all diagrams to create a vocabulary.
#. Assign tensors to each one of the words in the vocabulary, initialised randomly.
#. Training loop:

   a. Substitute the tensors from the vocabulary for the corresponding words in the diagram.

   b. Contract the diagram to get a result.

   c. Use the result to compute loss.

   d. Use loss to compute gradient and update tensors.

In the quantum case we do not explicitly have tensors, but :term:`circuit <quantum circuit>` parameters defining rotation angles on :term:`qubits <qubit>`, that need to be associated with concrete numbers; these are also represented by :term:`symbols <symbol>`.

The first part of this tutorial provides a short introduction to :term:`symbols <symbol>` and their use, while in the second part we will go through all stages of a complete experiment.

.. toctree::

    ../tutorials/training-symbols.ipynb
    ../tutorials/training-usecase.ipynb
