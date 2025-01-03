from enum import Enum

class TextType(Enum):
    Normal_text = True
    Bold_text = True
    Italic_text = True
    Code_text = True
    Links = True
    Images = True 


class TextNode(text, text_type, URL):
    def __init__(self):
        self.text = 'text content of the node'
        self.text_type = text_type
        self.url = URL
        

def __eq__():
    if TextNode == TextNode:
        return True
    
def __repr__():
    return print(f"{TextNode.text}, {TextNode.text_type.value()}, {TextNode.url}")
