import unittest

from htmlnode import HTMLNode

#more formal debugging
#calls your function and compares it against a static result

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "class": "my-class"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" class="my-class"')


if __name__ == "__main__":
    unittest.main()