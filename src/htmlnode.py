

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        #for prop in props:

        pass


#this block only runs if the file is run directly
if __name__ == '__main__':
    test_node = HTMLNode(
        tag="a",
        props={
            "href": "https://google.com",
            "class": "link-button"
        }
    )
    print(test_node.props)