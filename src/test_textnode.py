import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff(self):
        node3 = TextNode("what even is a node", TextType.ITALIC)
        node4 = TextNode("this is a node", TextType.LINK)
        self.assertNotEqual(node3, node4)

    #test text type enum
    def test_text_type_bold(self):
        node = TextNode(text="Hello World", text_type=TextType.BOLD)
        html_node = text_node_to_html_node(node)
        expected = LeafNode(tag="b", value="Hello World")
        self.assertEqual(html_node, expected)

    def test_text_type_link(self):
        node = TextNode(
            text="this is a LINK",
            text_type=TextType.LINK,
            url="www.google.com"
        )
        html_node = text_node_to_html_node(node)
        expected = LeafNode(
            tag="a",
            value="this is a LINK",
            props={"href": "www.google.com"}
        )
        self.assertEqual(html_node, expected)

    def test_text_type_code(self):
        node = TextNode(text="this is code", text_type=TextType.CODE)
        html_node = text_node_to_html_node(node)
        expected = LeafNode(tag="code", value="this is code")
        self.assertEqual(html_node, expected)

    def test_text_type_image(self):
        node = TextNode(
            text="this is alt text for an image",
            text_type=TextType.IMAGE,
            url="www.aol.com"
        )
        html_node = text_node_to_html_node(node)
        expected = LeafNode(
            tag="img",
            value="",
            props={
                "src": "www.aol.com",
                "alt": "this is alt text for an image"
            }
        )
        self.assertEqual(html_node, expected)

    def test_invalid_text_type(self):
        node = TextNode(text="Hello World", text_type="invalid_type")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
            
if __name__ == "__main__":
    unittest.main()