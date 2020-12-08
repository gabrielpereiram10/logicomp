"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """

from typing import Set, Tuple, Union

from formula import *
from functions import atoms


def truth_value(formula: Formula, interpretation: Set[Tuple[str, bool]]) -> Union[bool, None]:
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """

    if isinstance(formula, Atom):
        return formula.get_value(interpretation.copy())
    if isinstance(formula, Not):
        return Not(
            truth_value(formula.inner, interpretation)
        ).truth_value()
    if isinstance(formula, BinaryConnective):
        return type(formula)(
            truth_value(formula.left, interpretation),
            truth_value(formula.right, interpretation)
        ).truth_value()


def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def is_satisfiable(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========
