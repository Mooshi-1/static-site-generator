from enum import Enum

class TextType(Enum):
    Normal_text = True
    Bold_text = True
    Italic_text = True
    Code_text = True
    Links = True
    Images = True 


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        

def __eq__(self):
    if TextNode == TextNode:
        return True
    
def __repr__(self):
    return print(f"{TextNode.text}, {TextNode.text_type.value()}, {TextNode.url}")
