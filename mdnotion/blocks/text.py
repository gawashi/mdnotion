from collections.abc import Iterable

from .base import BaseBlock


class RichText(BaseBlock):
    """
    Rich text block.
    """

    _type = "text"

    def __init__(
        self,
        content: str,
        link: str | None = None,
        bold: bool = False,
        italic: bool = False,
        strikethrough: bool = False,
        underline: bool = False,
        code: bool = False,
        color: str = "default",
    ):
        super().__init__()
        self.content = content
        self.link = link

        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        self.code = code
        self.color = color

    def to_dict(self) -> dict:
        result = super().to_dict()

        result[self.block_type] = {"content": self.content}
        if self.link:
            result[self.block_type]["link"] = {"url": self.link}
            result["href"] = self.link
        result["annotations"] = {
            "bold": self.bold,
            "italic": self.italic,
            "strikethrough": self.strikethrough,
            "underline": self.underline,
            "code": self.code,
            "color": self.color,
        }
        result["plain_text"] = self.content

        return result


class Paragraph(BaseBlock):
    """
    Paragraph block.
    """

    _type = "paragraph"

    def __init__(
        self,
        rich_text: RichText | Iterable[RichText],
        color: str = "default",
        children=None,
    ):
        super().__init__(children=children)
        if isinstance(rich_text, RichText):
            rich_text = [rich_text]

        self.rich_text = rich_text
        self.color = color

    def to_dict(self) -> dict:
        result = super().to_dict()
        result[self.block_type] = {"rich_text": [child.to_dict() for child in self.rich_text]}
        result[self.block_type]["color"] = self.color

        return result


class Heading(Paragraph):
    """
    Heading block.
    """

    def __new__(cls, *args, **kwargs):
        if "level" in kwargs:
            level = kwargs["level"]
        else:
            level = args[1] if len(args) > 1 else None
            if level is None:
                raise TypeError("Heading.__new__() missing required argument: 'level'")

        if level <= 3:
            instance = super().__new__(cls)
            instance._type = f"heading_{level}"
            return instance
        else:
            # remove level
            kwargs.pop("level", None)
            if len(args) > 1:
                args = args[:1] + args[2:]

            # TODO: toggleable
            instance = Paragraph.__new__(Paragraph)
            Paragraph.__init__(instance, *args, **kwargs)

            return instance

    def __init__(
        self,
        rich_text: RichText | Iterable[RichText],
        level: int,
        color: str = "default",
        children=None,
        is_toggleable: bool = False,
    ):
        super().__init__(rich_text=rich_text, color=color, children=children)
        self.level = level
        self.is_toggleable = is_toggleable

    def to_dict(self) -> dict:
        result = super().to_dict()

        result[self.block_type]["is_toggleable"] = self.is_toggleable
        if self.is_toggleable and len(self.children) == 0:
            result["children"] = []

        return result
