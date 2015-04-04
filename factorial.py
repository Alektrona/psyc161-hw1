# Katherine Alfred Homework 1, 4/4/2015

from nose.tools import assert_equal


# Counts activations of factorial_recursive in stack until it hits the
# base case, where it'll return up the stack, multiplying n as it goes
def factorial_recursive(n):
    if (n == 0):
        return 1
    else:
        return n * factorial_recursive(n-1)


def test_factorial():
    assert_equal(factorial_recursive(1), 1)
    assert_equal(factorial_recursive(3), 6)
    assert_equal(factorial_recursive(6), 720)


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = int(raw_input("Please enter number of conditions: "))
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))
