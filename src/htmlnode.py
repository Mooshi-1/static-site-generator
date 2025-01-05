

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


#this block only runs if the file is run directly, add these for testing purposes
if __name__ == '__main__':
    test_node = HTMLNode(
        tag="a",
        props={
            "href": "https://google.com",
            "class": "link-button"
        }
    )
    print(test_node.props_to_html())
    print(test_node.props)