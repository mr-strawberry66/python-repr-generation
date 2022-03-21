"""Test SimpleRepr class."""
from .test_classes import TestClassConstants, TestInherited, TestNotInherited
from ..simple_repr import SimpleRepr


def test_is_inherited():
    """Test that SimpleRepr is a subclass of object."""
    assert issubclass(TestInherited, SimpleRepr)


def test_inherited_repr():
    """Test the __repr__ method of class inheriting the SimpleRepr class."""
    test_object = TestInherited("a", 1)
    assert repr(test_object) == "TestInherited(args=[arg_a='a', arg_b=1])"


def test_not_inherited_repr():
    """Test the __repr__ method of class not inheriting the SimpleRepr class."""
    test_object = TestNotInherited("a", 1)
    assert repr(test_object) == "TestNotInherited(args=[arg_a='a', arg_b=1])"


def test__check_type():
    """
    Test the _check_type method of SimpleRepr.

    Note the use of disable=W0212 to silence pylint
    complaining about testing a protected member.
    """
    assert SimpleRepr._check_type(1) == 1  # pylint: disable=W0212
    assert SimpleRepr._check_type("a") == "'a'"  # pylint: disable=W0212


def test__build_attrs():
    """Test the _build_attrs method of SimpleRepr."""
    attrs = {"arg_a": "a", "arg_b": "b"}.items()
    assert (
        SimpleRepr._build_attrs(attrs)  # pylint: disable=W0212
        == "args=[arg_a='a', arg_b='b']"
    )


def test__build_constants():
    """Test the _build_constants method of SimpleRepr."""
    consts = {"CONST_A": "Some Value"}.items()
    assert (
        SimpleRepr._build_constants(consts)  # pylint: disable=W0212
        == "consts=[CONST_A='Some Value']"
    )


def test_make_repr():
    """Test the make_repr method of SimpleRepr."""
    test_object = TestNotInherited("a", 1)
    assert (
        SimpleRepr.make_repr(test_object)
        == "TestNotInherited(args=[arg_a='a', arg_b=1])"
    )
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


def test_repr_with_class_constants():
    """Test that a class with constants returns the correct string."""
    test_object = TestClassConstants("a", 1)
    assert (
        repr(test_object)
        == "TestClassConstants(consts=[CONST_A='Some Value'], "
        + "args=[arg_a='a', arg_b=1])"
    )
