import os, sys
from MutationTesting.mutationtesting.Polynomial import Polynomial  # Import the Polynomial class from your module
import unittest

def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]

    poly1 = Polynomial([])
    assert poly1.coefficients == []

    poly2 = Polynomial(None)
    assert poly2.coefficients == []


def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""

    poly = Polynomial([1, 0, -3])  # coefficients: [1, 0, -3]
    result = str(poly)
    assert result == "1x^2 + -3"

    poly4 = Polynomial([1])
    assert str(poly4) == "1"

    poly5 = Polynomial([])
    assert str(poly5) == "0"

def test_add():
    # Test addition with polynomials of the same length
    poly1 = Polynomial([1, 2, 3])  # coefficients: [1, 2, 3]
    poly2 = Polynomial([4, 5, 6])  # coefficients: [4, 5, 6]
    result = poly1 + poly2
    assert result.coefficients == [5, 7, 9]  # Check the resulting coefficients

    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([])
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 0, 2]

    # Test addition with both empty polynomials
    poly1 = Polynomial([])  # coefficients: []
    poly2 = Polynomial([])  # coefficients: []
    result = poly1 + poly2
    assert result.coefficients == []  # Check the resulting coefficients

    # Test addition with other polynomial having length None
    poly1 = Polynomial([1, 2, 3])  # coefficients: [1, 2, 3]
    poly2 = Polynomial(None)  # coefficients: None
    result = poly1 + poly2
    # Expected behavior could vary based on your implementation,
    # for example, handling None as an empty polynomial.
    assert result.coefficients == [1, 2, 3]  # Check the resulting coefficients
def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3,-1, 3]

def test_mul():
    # Test multiplication with two empty polynomials
    poly1 = Polynomial([])
    poly2 = Polynomial([])
    result = poly1 * poly2
    assert result.coefficients == []

    # Test multiplication with a zero polynomial and another polynomial
    poly1 = Polynomial([0])
    poly2 = Polynomial([1, 2, 3])
    result = poly1 * poly2
    assert result.coefficients == [0, 0, 0]

    # Test multiplication with identity polynomial and another polynomial
    poly1 = Polynomial([1])
    poly2 = Polynomial([4, 5, 6])
    result = poly1 * poly2
    assert result.coefficients == [4, 5, 6]

    # Test multiplication with arbitrary polynomials
    poly1 = Polynomial([1, 2, 3])
    poly2 = Polynomial([4, 5])
    result = poly1 * poly2
    assert result.coefficients == [4, 13, 22, 15]

def test_evaluate():

    # Test evaluation of an empty polynomial
    poly = Polynomial([])
    result = poly.evaluate(5)  # Evaluate at x = 5 (arbitrary value)
    assert result == 0  # Expected result when evaluating an empty polynomial is 0


    # Test evaluation of a polynomial with a single term
    poly = Polynomial([2])  # Coefficients: [2]
    result = poly.evaluate(3)  # Evaluate at x = 3
    assert result == 2  # Expected result for a single term polynomial is the coefficient itself


    # Test evaluation of a polynomial with multiple terms
    poly = Polynomial([1, 0, 3])  # Coefficients: [1, 0, 3]
    result = poly.evaluate(2)  # Evaluate at x = 2
    assert result == 13  # Expected result for the given polynomial at x = 2 is 13


    # Test evaluation of a polynomial with a negative coefficient
    poly = Polynomial([1, 0, -3])  # Coefficients: [1, 0, -3]
    result = poly.evaluate(3)  # Evaluate at x = 3
    assert result == -24  # Expected result for the given polynomial at x = 3 is -24

def test_derivative():

    # Test derivative of an empty polynomial
    poly = Polynomial([])
    result = poly.get_derivative_coefficients()
    assert result == []  # Expected result when getting derivative of an empty polynomial is an empty list


    # Test derivative of a polynomial with a single term
    poly = Polynomial([2])  # Coefficients: [2]
    result = poly.get_derivative_coefficients()
    assert result == []  # Expected result for the derivative of a single term polynomial is an empty list


    # Test derivative of a polynomial with multiple terms
    poly = Polynomial([1, 0, 3])  # Coefficients: [1, 0, 3]
    result = poly.get_derivative_coefficients()
    assert result == [2, 0]  # Expected result for the derivative of the given polynomial is [0, 6]


    # Test derivative of a polynomial with a negative coefficient
    poly = Polynomial([1, 0, -3])  # Coefficients: [1, 0, -3]
    result = poly.get_derivative_coefficients()
    assert result == [2, 0, 0]  # Expected result for the derivative of the given polynomial is [0, -6]
def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6

def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0**0.5) < 1e-6

def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6
   

