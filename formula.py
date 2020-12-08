"""This module is designed to define formulas in propositional logic.
For example, the following piece of code creates an object representing (p v s).

formula1 = Or(Atom('p'), Atom('s'))


As another example, the piece of code below creates an object that represents (p → (p v s)).

formula2 = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
"""

from abc import abstractmethod
from typing import Union, Set, Tuple, Sized


class Formula:
    ...


class Connective:
    @abstractmethod
    def truth_value(self) -> Union[bool, None]:
        raise NotImplemented


class BinaryConnective(Connective):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Atom(Formula):
    """
    This class represents propositional logic variables.
    """

    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_value(self, interpretation_copy: Set[Tuple[str, bool]]) -> Union[bool, None]:
        if self.__is_empty(interpretation_copy):
            return None
        valuation = interpretation_copy.pop()
        if valuation[0] == self.name:
            return valuation[1]
        return self.get_value(interpretation_copy)

    @staticmethod
    def __is_empty(iterable: Sized) -> bool:
        return len(iterable) == 0

    def __repr__(self):
        return str(self.name)

    def __eq__(self, other):
        return isinstance(other, Atom) and other.name == self.name

    def __hash__(self):
        return hash((self.name, 'atom'))


class Implies(BinaryConnective, Formula):

    def __init__(self, left, right):
        super().__init__(left, right)

    def truth_value(self) -> Union[bool, None]:
        if self.left is False or self.right is True:
            return True
        if self.left is True and self.right is False:
            return False
        return None

    def __repr__(self):
        return "(" + self.left.__str__() + " " + u"\u2192" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, Implies) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'implies'))


class Not(Connective, Formula):

    def __init__(self, inner):
        super().__init__()
        self.inner = inner

    def truth_value(self) -> Union[bool, None]:
        if isinstance(self.inner, bool):
            return not self.inner
        return None

    def __repr__(self):
        return "(" + u"\u00ac" + str(self.inner) + ")"

    def __eq__(self, other):
        return isinstance(other, Not) and other.inner == self.inner

    def __hash__(self):
        return hash((hash(self.inner), 'not'))


class And(BinaryConnective, Formula):

    def __init__(self, left, right):
        super().__init__(left, right)

    def truth_value(self) -> Union[bool, None]:
        if self.left is True and self.right is True:
            return True
        if self.left is False or self.right is False:
            return False
        return None

    def __repr__(self):
        return "(" + self.left.__str__() + " " + u"\u2227" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, And) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'and'))


class Or(BinaryConnective, Formula):

    def __init__(self, left, right):
        super().__init__(left, right)

    def truth_value(self) -> Union[bool, None]:
        if self.left is True or self.right is True:
            return True
        if self.left is False and self.right is False:
            return False
        return None

    def __repr__(self):
        return "(" + self.left.__str__() + " " + u"\u2228" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, Or) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'or'))


class Iff:
    """
    Describes the 'if and only if' logical connective (<->) from propositional logic.
    Unicode value for <-> is 2194.
    """
    pass


class Xor:
    """
    Describes the xor (exclusive or) logical connective from propositional logic.
    Unicode value for xor is 2295.
    """
    pass
