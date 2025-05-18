from collections.abc import Iterable

from .base import BaseBlock
from .text import RichText


class BulletedListItem(BaseBlock):
    """
    Bulleted list item block.
    """

    _type = "bulleted_list_item"

    def __init__(
        self,
        rich_text: RichText | Iterable[RichText],
        color: str = "default",
        children=None,
    ):
        super().__init__()
        if isinstance(rich_text, RichText):
            rich_text = [rich_text]

        self.rich_text = rich_text
        self.color = color

        self.children = children

    def to_dict(self) -> dict:
        result = super().to_dict()
        result[self.block_type] = {"rich_text": [rt.to_dict() for rt in self.rich_text]}

        if self.children is not None:
            result[self.block_type]["children"] = [child.to_dict() for child in self.children]

        return result


class NumberedListItem(BulletedListItem):
    """
    Numbered list item block.
    """

    _type = "numbered_list_item"
