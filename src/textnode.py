from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image' 


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        

    def __eq__(self, other):
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b",value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i",value=text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code",value=text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a",value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img",value="", props={"src": text_node.url, "alt": text_node.text})    

    else:
        raise Exception("Not valid")
    

if __name__ == "__main__":
    test_text1 = TextNode(text="Hello World", text_type=TextType.BOLD)
    test_text2 = TextNode(text="this is a LINK", text_type=TextType.LINK, url="www.google.com")
    test_text3 = TextNode(text="this is code", text_type=TextType.CODE)
    test_text4 = TextNode(text="this is alt text for an image", text_type=TextType.IMAGE, url="www.aol.com")
    
    print(text_node_to_html_node(test_text1))
    print(text_node_to_html_node(test_text2))
    print(text_node_to_html_node(test_text3))
    print(text_node_to_html_node(test_text4))