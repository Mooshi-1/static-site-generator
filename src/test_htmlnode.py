import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    #parentnode tests
    #more advanced children nodes
    def test_parentnode_missing_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag=None, children=[LeafNode("b", "Bold text")])
            node.to_html()

    def test_parentnode_missing_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag="div", children=None)
            node.to_html()

    def test_parentnode_valid_children(self):
        node = ParentNode(
            tag="div",
            children=[
                LeafNode("b", "Bold text"),
                " and some ",
                LeafNode("i", "italic text")
            ]
        )
        expected_html = "<div><b>Bold text</b> and some <i>italic text</i></div>"
        self.assertEqual(node.to_html(), expected_html)



if __name__ == "__main__":
    
    unittest.main()