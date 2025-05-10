from mistune import BaseRenderer, BlockState

from mdnotion.blocks import (
    bulleted_list_item_block,
    code_block,
    heading_block,
    numbered_list_item_block,
    paragraph_block,
    text_block,
)


class NotionRenderer(BaseRenderer):
    NAME = "notion"

    def render_tokens(self, tokens, state) -> list[dict]:
        results = []
        for res in self.iter_tokens(tokens, state):
            if isinstance(res, list):
                results.extend(res)
            else:
                results.append(res)

        return results

    # Block level methods
    def heading(self, token: dict, state: BlockState) -> dict:
        attrs = token["attrs"]
        rich_text = self.render_tokens(token["children"], state)
        return heading_block(rich_text, level=attrs["level"])

    def paragraph(self, token: dict, state: BlockState) -> dict:
        rich_text = self.render_tokens(token["children"], state)
        return paragraph_block(rich_text)

    def list(self, token: dict, state: BlockState) -> list:
        attrs = token["attrs"]
        for t in token["children"]:
            t["type"] = "numbered_list_item" if attrs["ordered"] else "bulleted_list_item"

        return self.render_tokens(token["children"], state)

    def _list_item(self, token: dict, state: BlockState) -> tuple:
        for t in token["children"]:
            if t["type"] == "paragraph":
                t["type"] = "block_text"

        results = self.render_tokens(token["children"], state)

        rich_text = []
        childrens = []
        for res in results:
            if res["type"] == "text":
                rich_text.append(res)
            else:
                childrens.append(res)

        return rich_text, childrens

    def bulleted_list_item(self, token: dict, state: BlockState) -> dict:
        rich_text, childrens = self._list_item(token, state)
        return bulleted_list_item_block(rich_text, children=childrens)

    def numbered_list_item(self, token: dict, state: BlockState) -> dict:
        rich_text, childrens = self._list_item(token, state)
        return numbered_list_item_block(rich_text, children=childrens)

    def block_code(self, token: dict, state: BlockState) -> dict:
        attrs = token["attrs"]
        return code_block(self.text(token, state), language=attrs["info"])

    def blank_line(self, token: dict, state: BlockState) -> dict:
        return paragraph_block(text_block(" "))

    # Inline level methods
    def text(self, token: dict, state: BlockState) -> dict:
        content = token.get("raw", "")

        attrs = token["attrs"] if "attrs" in token else {}
        return text_block(content, **attrs)

    def strong(self, token: dict, state: BlockState) -> list:
        for t in token["children"]:
            t["attrs"] = {"bold": True}
        return self.render_tokens(token["children"], state)

    def emphasis(self, token: dict, state: BlockState) -> list:
        for t in token["children"]:
            t["attrs"] = {"italic": True}
        return self.render_tokens(token["children"], state)

    def link(self, token: dict, state: BlockState) -> list:
        for t in token["children"]:
            t["attrs"] = {"link": token["attrs"]["url"]}
        return self.render_tokens(token["children"], state)

    def codespan(self, token: dict, state: BlockState) -> dict:
        attrs = token["attrs"] if "attrs" in token else {}

        attrs["code"] = True
        return text_block(token["raw"], **attrs)

    def block_text(self, token: dict, state: BlockState) -> list:
        return self.render_tokens(token["children"], state)

    def linebreak(self, token: dict, state: BlockState) -> dict:
        return text_block(" ")

    def softbreak(self, token: dict, state: BlockState) -> dict:
        return text_block(" ")
