"""Store classes used for testing the simple_repr module."""
from ..simple_repr import SimpleRepr


class TestInherited(SimpleRepr):  # pylint: disable=R0903
    """Class used to test SimpleRepr module."""

    def __init__(self, arg_a: str, arg_b: int):
        """Initialise instance."""
        self.arg_a = arg_a
        self.arg_b = arg_b


TestInherited.__test__ = False


class TestNotInherited:  # pylint: disable=R0903
    """Class used to test SimpleRepr module."""

    def __init__(self, arg_a: str, arg_b: int):
        """Initialise instance."""
        self.arg_a = arg_a
        self.arg_b = arg_b

    def __repr__(self) -> str:
        """Return string representation of instance."""
        return SimpleRepr.make_repr(self)


TestNotInherited.__test__ = False
