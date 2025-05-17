from unittest import TestCase

from mdnotion.blocks.base import BaseBlock


class TestBaseBlock(TestCase):
    block_type = "base"
    simple_dict = {"type": block_type}

    def test_initialize(self):
        """
        Test the initialization of BaseBlock.
        """
        block = BaseBlock()
        self.assertEqual(block.block_type, self.block_type)
        self.assertEqual(block.children, [])

        block_with_children = BaseBlock(children=[BaseBlock()])
        self.assertEqual(len(block_with_children.children), 1)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseBlock.
        """

        block = BaseBlock()
        self.assertEqual(block.to_dict(), self.simple_dict)

        dict_with_children = self.simple_dict.copy()
        dict_with_children["children"] = [self.simple_dict]
        block_with_children = BaseBlock(children=[BaseBlock()])
        self.assertEqual(block_with_children.to_dict(), dict_with_children)
