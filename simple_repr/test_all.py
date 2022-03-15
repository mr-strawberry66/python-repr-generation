"""Test SimpleRepr class."""
try:
    from .simple_repr import SimpleRepr
except ImportError:
    from simple_repr import SimpleRepr


class TestInherited(SimpleRepr):
    """Class used to test SimpleRepr module."""

    def __init__(self, a: str, b: int):
        """Initialise instance."""
        self.a = a
        self.b = b


class TestNotInherited:
    """Class used to test SimpleRepr module."""

    def __init__(self, a: str, b: int):
        """Initialise instance."""
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        """Return string representation of instance."""
        return SimpleRepr.make_repr(self)


def test_is_inherited():
    """Test that SimpleRepr is a subclass of object."""
    assert issubclass(TestInherited, SimpleRepr)


def test_inherited_repr():
    """Test the __repr__ method of class inheriting the SimpleRepr class."""
    test_object = TestInherited("a", 1)
    assert repr(test_object) == "TestInherited(a='a', b=1)"


def test_not_inherited_repr():
    """Test the __repr__ method of class not inheriting the SimpleRepr class."""
    test_object = TestNotInherited("a", 1)
    assert repr(test_object) == "TestNotInherited(a='a', b=1)"


def test__check_type():
    """Test the _check_type method of SimpleRepr."""
    assert SimpleRepr._check_type(1) == 1
    assert SimpleRepr._check_type("a") == "'a'"
