# Make sure Python can import from the src/ folder when CI runs from repo root
import sys, os
sys.path.append(os.path.abspath("src"))

from math_ops import add

def test_add():
    assert add(2, 3) == 5


# tests/test_math_ops.py
def test_subtract():
    from math_ops import subtract
    assert subtract(5, 3) == 2

