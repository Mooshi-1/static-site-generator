import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff(self):
        node3 = TextNode("what even is a node", TextType.ITALIC)
        node4 = TextNode("this is a node", TextType.LINK)
        self.assertNotEqual(node3, node4)





if __name__ == "__main__":
    unittest.main()