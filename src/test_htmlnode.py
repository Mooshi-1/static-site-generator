import unittest

from htmlnode import HTMLNode, LeafNode

#more formal debugging
#calls your function and compares it against a static result

#for reference, ctrl k then ctrl c to comment out
# class HTMLNode():
#     def __init__(self, tag=None, value=None, children=None, props=None):
#         self.tag = tag
#         self.value = value
#         self.children = children
#         self.props = props

class TestHTMLNode(unittest.TestCase):
    #HTML node tests
    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "class": "my-class"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" class="my-class"')

    #LeafNode tests
    #note, do not pass in children param at all, even as None
    def test_leafnode_props(self):
        node = LeafNode(tag="a", value="testing no props", props=None)
        self.assertEqual(node.to_html(), '<a>testing no props</a>')

    def test_leafnode_proper(self):
        node = LeafNode(tag="a", value="testing expected input/output", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">testing expected input/output</a>')

    def test_leafnode_notag(self):
        node = LeafNode(tag=None, value="No tag", props=None)
        self.assertEqual(node.to_html(), 'No tag')
    
    def test_leafnode_novalue(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value=None, props=None)
            node.to_html()


if __name__ == "__main__":
    
    unittest.main()