def text_block(
    content: str,
    link: str | None = None,
    bold: bool = False,
    italic: bool = False,
    strikethrough: bool = False,
    underline: bool = False,
    code: bool = False,
    color: str = "default",
    **kwargs,
) -> dict:
    block = {
        "type": "text",
        "text": {
            "content": content,
        },
        "annotations": {
            "bold": bold,
            "italic": italic,
            "strikethrough": strikethrough,
            "underline": underline,
            "code": code,
            "color": color,
        },
        "plain_text": content,
        "href": link,
    }
    if link:
        block["text"]["link"] = {"url": link}

    return block


def heading_block(
    rich_text: list[dict] | dict,
    level: int = 1,
    color: str = "default",
    is_toggleable: bool = False,
    children=None,
) -> dict:
    if isinstance(rich_text, dict):
        rich_text = [rich_text]

    if level <= 3:
        block = {
            "type": f"heading_{level}",
            f"heading_{level}": {
                "rich_text": rich_text,
                "color": color,
                "is_toggleable": is_toggleable,
            },
        }
        if is_toggleable and children:
            block[f"heading_{level}"]["children"] = children
    else:
        for t in rich_text:
            t["annotations"]["bold"] = True
        block = paragraph_block(rich_text, color, children=children)

    return block


def paragraph_block(rich_text: list[dict] | dict, color: str = "default", children=None) -> dict:
    if isinstance(rich_text, dict):
        rich_text = [rich_text]

    block = {
        "type": "paragraph",
        "paragraph": {
            "rich_text": rich_text,
            "color": color,
        },
    }
    if children:
        block["paragraph"]["children"] = children

    return block


def bulleted_list_item_block(
    rich_text: list[dict] | dict, color: str = "default", children: list | None = None
) -> dict:
    if isinstance(rich_text, dict):
        rich_text = [rich_text]

    block = {
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": rich_text, "color": color},
    }
    if children:
        block["bulleted_list_item"]["children"] = children

    return block


def numbered_list_item_block(
    rich_text: list[dict] | dict, color: str = "default", children: list | None = None
) -> dict:
    if isinstance(rich_text, dict):
        rich_text = [rich_text]

    block = {
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": rich_text,
            "color": color,
        },
    }
    if children:
        block["numbered_list_item"]["children"] = children

    return block


def code_block(
    rich_text: list[dict] | dict,
    language: str = "plaintext",
    caption: list[dict] | None = None,
) -> dict:
    if isinstance(rich_text, dict):
        rich_text = [rich_text]

    block = {
        "type": "code",
        "code": {
            "rich_text": rich_text,
            "language": language,
        },
    }
    if caption:
        block["code"]["caption"] = caption

    return block


def divider_block() -> dict:
    return {"type": "divider", "divider": {}}


def embed_block(url: str) -> dict:
    return {"type": "embed", "embed": {"url": url}}


def toc_block(color="default") -> dict:
    return {"type": "table_of_contents", "table_of_contents": {"color": color}}
