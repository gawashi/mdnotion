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
        result[self.block_type] = {}

        return result


class Divider(BaseBlock):
    """
    A divider block in Notion.
    """

    _type = "divider"


class Toc(BaseBlock):
    """
    A table of contents block in Notion.
    """

    _type = "table_of_contents"

    def __init__(self, color: str = "default"):
        super().__init__()
        self.color = color

    def to_dict(self) -> dict:
        result = super().to_dict()
        result[self.block_type]["color"] = self.color
        return result
