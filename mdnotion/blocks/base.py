from collections.abc import Iterable


class BaseBlock:
    """
    Base class for all blocks.
    """

    _type = "base"

    def __init__(self, children: Iterable | None = None):
        self.children = children if children is not None else []

    @property
    def block_type(self) -> str:
        return self._type

    def to_dict(self) -> dict:
        """
        Convert the block to a dictionary representation.
        """
        result = {"type": self.block_type}
        if self.children:
            result["children"] = [child.to_dict() for child in self.children]

        return result
