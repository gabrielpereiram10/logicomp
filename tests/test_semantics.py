import unittest

from logicomp.propositional_logic.semantics import *
from logicomp.propositional_logic.formula import *


class TestSemantics(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Atom('p')
        self.q = Atom('q')
        self.r = Atom('r')
        self.s = Atom('s')

    def test_truth_value_for_atom(self):
        interpretation = [
            {(self.p.name, True)}, {(self.p.name, False)}
        ]
        expected = [
            True, False
        ]
        for i in range(len(interpretation)):
            with self.subTest(i=i):
                self.assertEqual(expected[i], truth_value(self.p, interpretation[i]))

    def test_truth_value_for_negation_connective(self):
        formula = Not(self.p)
        interpretation = [
            {(self.p.name, True)}, {(self.p.name, False)}
        ]
        expected = [
            False, True
        ]
        for i in range(len(interpretation)):
            with self.subTest(i=i):
                self.assertEqual(expected[i], truth_value(formula, interpretation[i]))

    def test_truth_value_for_binary_connective(self):
        formulas = [
            Implies(self.p, self.q),
            Or(self.p, self.q),
            And(self.p, self.q)
        ]
        interpretation = [
            {(self.p.name, False)}, {(self.q.name, True)}, {(self.q.name, True)}
        ]
        expected = [
            True, True, None
        ]
        for i in range(len(interpretation)):
            with self.subTest(i=i):
                self.assertEqual(expected[i], truth_value(formulas[i], interpretation[i]))

    def test_truth_value_for_more_difficult_formula(self):
        formula = Not(Implies(self.p, And(Not(self.p), self.q)))
        interpretation = [
            {(self.p.name, True)}, {(self.p.name, False)}, {(self.q.name, True)}
        ]
        expected = [
            True, False, None
        ]
        for i in range(len(interpretation)):
            with self.subTest(i=i):
                self.assertEqual(expected[i], truth_value(formula, interpretation[i]))


if __name__ == '__main__':
    unittest.main()
