from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import ComparisonMixin


class Attribute(XPathBase, ComparisonMixin):
    def __init__(self, identifier='*', parent=None):
        self.identifier = identifier
        super(Attribute, self).__init__(parent=parent)

    def render_object(self, child=None):
        return '@{identifier}'.format(identifier=self.identifier)
