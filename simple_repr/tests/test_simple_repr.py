"""Test SimpleRepr class."""
from .test_classes import TestInherited, TestNotInherited
from ..simple_repr import SimpleRepr


def test_is_inherited():
    """Test that SimpleRepr is a subclass of object."""
    assert issubclass(TestInherited, SimpleRepr)


def test_inherited_repr():
    """Test the __repr__ method of class inheriting the SimpleRepr class."""
    test_object = TestInherited("a", 1)
    assert repr(test_object) == "TestInherited(arg_a='a', arg_b=1)"


def test_not_inherited_repr():
    """Test the __repr__ method of class not inheriting the SimpleRepr class."""
    test_object = TestNotInherited("a", 1)
    assert repr(test_object) == "TestNotInherited(arg_a='a', arg_b=1)"


def test__check_type():
    """
    Test the _check_type method of SimpleRepr.

    Note the use of disable=W0622 to silence pylint
    complaining about testing a protected member.
    """
    assert SimpleRepr._check_type(1) == 1  # pylint: disable=W0212
    assert SimpleRepr._check_type("a") == "'a'"  # pylint: disable=W0212


def test_make_repr():
    """Test the make_repr method of SimpleRepr."""
    test_object = TestNotInherited("a", 1)
    assert SimpleRepr.make_repr(test_object) == "TestNotInherited(arg_a='a', arg_b=1)"
    assert SimpleRepr.make_repr(1) == "1"


def test_make_repr_returns_str():
    """Test that the make_repr method returns a string."""
    test_object = TestNotInherited("a", 1)
    assert isinstance(SimpleRepr.make_repr(test_object), str)
    assert isinstance(SimpleRepr.make_repr("a"), str)
    assert isinstance(SimpleRepr.make_repr(1), str)
    assert isinstance(SimpleRepr.make_repr({"a": 1}), str)
    assert isinstance(SimpleRepr.make_repr(["a", 1]), str)
    assert isinstance(SimpleRepr.make_repr(("a", 1)), str)
    assert isinstance(SimpleRepr.make_repr(any), str)
    assert isinstance(SimpleRepr.make_repr(...), str)
