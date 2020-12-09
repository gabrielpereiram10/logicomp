"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """

from logicomp.propositional_logic.formula import *
from logicomp.propositional_logic.functions import atoms


def truth_value(formula: Formula, interpretation: Set[Tuple[Atom, bool]]) -> Union[bool, None]:
    """
    Determines the true value of a formula for an interpretation (evaluation) complete or partial.
    An interpretation can be defined as a set of tuples. For example, {(Atom('p'), True)}.
    """

    if isinstance(formula, Atom):
        return formula.get_value(interpretation)
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


def is_valid(formula: Formula) -> bool:
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""

    if is_satisfiable(Not(formula)):
        return False
    return True


def is_satisfiable(formula: Formula) -> Union[Set[Tuple[Atom, bool]], bool]:
    """
    Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False.
    """

    set_atoms = atoms(formula)
    interpretation = get_partial_interpretation(formula)
    if interpretation:
        set_atoms = new_set_atoms(set_atoms, interpretation)
        result = sat(formula, set_atoms, interpretation)
    else:
        result = sat(formula, set_atoms, set())
    if result:
        return result
    return False


def get_partial_interpretation(formula: Formula) -> Union[Set[Tuple[Atom, bool]], None]:
    """
    Returns a partial interpretation if possible. Otherwise, it returns None.
    """

    if isinstance(formula, Atom):
        return {(formula, True)}
    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return {(formula.inner, False)}
    if isinstance(formula, And):
        left = get_partial_interpretation(formula.left)
        right = get_partial_interpretation(formula.right)
        if left:
            if right:
                return left.union(right)
            return left
        if right:
            return right
        return None


def new_set_atoms(set_atoms: Set[Atom], interpretation: Set[Tuple[Atom, bool]]):
    return set(filter(
        lambda atom:
            not (interpretation.issuperset({(atom, True)}) or interpretation.issuperset({(atom, False)})),
            set_atoms
    ))


def sat(formula: Formula, set_atoms: Set[Atom], interpretation: Union[Set[Tuple[Atom, bool]], Set]) \
        -> Union[Set[Tuple[Atom, bool]], bool]:

    if is_empty(set_atoms):
        if truth_value(formula, interpretation):
            return interpretation
        return False
    # Gera cópias
    set_atoms_copy = set_atoms.copy()
    atom = set_atoms_copy.pop()
    interpretation_copy = interpretation.copy()

    interpretation1 = interpretation_copy.union({(atom, True)})
    interpretation2 = interpretation_copy.union({(atom, False)})

    result = sat(formula, set_atoms_copy, interpretation1)
    if result:
        return result
    return sat(formula, set_atoms_copy, interpretation2)


def is_empty(obj: Sized) -> bool:
    return len(obj) == 0
