from xpath_dsl.base import XPathBase
from xpath_dsl.comparison import Equals


class Attribute(XPathBase):
    def __init__(self, identifier='*', parent=None):
        self.identifier = identifier
        super(Attribute, self).__init__(parent=parent)

    def render_object(self):
        return '@{identifier}'.format(identifier=self.identifier)

    def equals(self, value):
        return Equals(value, parent=self)
