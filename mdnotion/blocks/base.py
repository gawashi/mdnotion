class BaseBlock:
    """
    Base class for all blocks.
    """

    _type = "base"

    def __init__(self):
        pass

    @property
    def block_type(self) -> str:
        return self._type

    def to_dict(self) -> dict:
        """
        Convert the block to a dictionary representation.
        """
        result = {"type": self.block_type}
        return result
