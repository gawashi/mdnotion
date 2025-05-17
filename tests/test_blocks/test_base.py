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

    def test_to_dict(self):
        """
        Test the to_dict method of BaseBlock.
        """

        block = BaseBlock()
        self.assertEqual(block.to_dict(), self.simple_dict)
