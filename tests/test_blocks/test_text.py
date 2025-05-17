from unittest import TestCase

from mdnotion.blocks import Heading, Paragraph, RichText


def generate_default_rich_text(content: str) -> dict:
    result = {
        "type": "text",
        "text": {"content": content},
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": "default",
        },
        "plain_text": content,
    }

    return result


class TestRichText(TestCase):
    block_type = "text"

    def test_to_dict(self):
        text = "Hello, World!"
        block = RichText(content=text)

        expected_dict = generate_default_rich_text(text)
        self.assertEqual(block.to_dict(), expected_dict)

        # Test with link
        link = "https://example.com"

        expected_dict = generate_default_rich_text(text)
        expected_dict[self.block_type]["link"] = {"url": link}
        expected_dict["href"] = link

        block_with_link = RichText(content=text, link=link)
        self.assertEqual(block_with_link.to_dict(), expected_dict)


class TestParagraph(TestCase):
    block_type = "paragraph"

    def test_to_dict(self):
        text = "Hello, World!"
        rich_text = RichText(content=text)

        block = Paragraph(rich_text=rich_text)
        expected_dict = {
            "type": self.block_type,
            self.block_type: {
                "rich_text": [rich_text.to_dict()],
                "color": "default",
            },
        }
        self.assertEqual(block.to_dict(), expected_dict)

        # Test multiple rich text objects
        rich_text_list = [
            RichText(content="Hello"),
            RichText(content="World"),
        ]
        block = Paragraph(rich_text=rich_text_list)
        expected_dict = {
            "type": self.block_type,
            self.block_type: {
                "rich_text": [rt.to_dict() for rt in rich_text_list],
                "color": "default",
            },
        }
        self.assertEqual(block.to_dict(), expected_dict)


class TestHeading(TestCase):
    block_type = "heading_1"

    def test_initialize(self):
        text = "Hello, World!"
        rich_text = RichText(content=text)

        heading1 = Heading(rich_text=rich_text, level=1)
        self.assertEqual(heading1.block_type, "heading_1")
        self.assertEqual(heading1.level, 1)

        heading2 = Heading(rich_text=rich_text, level=2)
        self.assertEqual(heading2.block_type, "heading_2")
        self.assertEqual(heading2.level, 2)

        heading3 = Heading(rich_text=rich_text, level=3)
        self.assertEqual(heading3.block_type, "heading_3")
        self.assertEqual(heading3.level, 3)

        heading4 = Heading(rich_text=rich_text, level=4)
        self.assertIsInstance(heading4, Paragraph)
        self.assertEqual(heading4.block_type, "paragraph")

        Heading(rich_text, 4)  # Test with positional arguments

    def test_to_dict(self):
        text = "Hello, World!"
        rich_text = RichText(content=text)

        heading = Heading(rich_text=rich_text, level=1)
        expected_dict = {
            "type": heading.block_type,
            heading.block_type: {
                "rich_text": [rich_text.to_dict()],
                "color": "default",
                "is_toggleable": False,
            },
        }

        self.assertEqual(heading.to_dict(), expected_dict)

        # Test heanding 4
        heading4 = Heading(rich_text, level=4)
        expected_dict = {
            "type": "paragraph",
            "paragraph": {
                "rich_text": [rich_text.to_dict()],
                "color": "default",
            },
        }

        self.assertEqual(heading4.to_dict(), expected_dict)
