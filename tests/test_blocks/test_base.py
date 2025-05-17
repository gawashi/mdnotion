from unittest import TestCase

from mdnotion.blocks.base import BaseBlock


class TestBase(TestCase):
    def test_to_dict(self):
        """
        Test the to_dict method of BaseBlock.
        """
        simple_dict = {"type": "base"}

        block = BaseBlock()
        self.assertEqual(block.to_dict(), simple_dict)

        block = BaseBlock(children=[BaseBlock()])
        self.assertEqual(block.to_dict(), {"type": "base", "children": [simple_dict]})
