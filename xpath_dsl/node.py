from xpath_dsl.base import XPathBase
from xpath_dsl.conditional import Where


class Node(XPathBase):
    def __init__(self, identifier='*', parent=None):
        self.identifier = identifier
        super(Node, self).__init__(parent=parent)

    def render_object(self):
        return self.identifier

    def where(self, *conditions):
        return Where(*conditions, parent=self)
