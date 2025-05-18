from unittest import TestCase

from mdnotion.blocks.base import BaseBlock, Divider


class TestBaseBlock(TestCase):
    block_type = "base"
    simple_dict = {"type": block_type, block_type: {}}

    def test_to_dict(self):
        """
        Test the to_dict method of BaseBlock.
        """

        block = BaseBlock()
        self.assertEqual(block.block_type, self.block_type)
        self.assertEqual(block.to_dict(), self.simple_dict)


class TestDivider(TestCase):
    block_type = "divider"
    simple_dict = {"type": block_type, block_type: {}}

    def test_to_dict(self):
        """
        Test the to_dict method of Divider.
        """

        block = Divider()
        self.assertEqual(block.block_type, self.block_type)
        self.assertEqual(block.to_dict(), self.simple_dict)
