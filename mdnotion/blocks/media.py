from .base import BaseBlock


class Embed(BaseBlock):
    """
    An embed block in Notion.
    """

    _type = "embed"

    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def to_dict(self) -> dict:
        result = super().to_dict()
        result[self.block_type]["url"] = self.url
        return result
