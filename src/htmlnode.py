

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        #join key and value with a space inbetween
        #calling the string doesn't include the quotes automatically, just raw characters
        #square brackets are creating a list of formatted strings
        #handle None case with if statement
        if self.props is None:
            return ""
        return (" "+" ".join([f'{key}="{value}"' for key, value in self.props.items()]))
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag 
            and self.value == other.value 
            and self.children == other.children 
            and self.props == other.props
    )
    
#leaf node doesn't accept all params from parent class
#it must have values for tag and value, children is empty (must be none), and props are    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        convert = self.props_to_html()
        return f"<{self.tag}{convert}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
            super().__init__(tag, None, children, props)     
        #tag and children not optional  
        #no value

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node tag is missing")
        if self.children is None:
            raise ValueError("Node children missing")
        convert = self.props_to_html()
        
            
        total_children = ""
        for element in self.children:
            #hasattr is a way to check if it's dealing with an object or a string
            #(element, 'to_html') searches for the to_html method and prints True or False
            if hasattr(element, 'to_html'):
                total_children += element.to_html()
            else:
                total_children += element

        
        return f"<{self.tag}{convert}>{total_children}</{self.tag}>"
    



#this block only runs if the file is run directly, add these for testing purposes
if __name__ == '__main__':
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    node.to_html()