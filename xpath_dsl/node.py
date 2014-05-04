from xpath_dsl.base import XPathBase
from xpath_dsl.conditional import Where
from xpath_dsl.mixins import ComparisonMixin


class NodeBase(XPathBase):
    pass


class Node(XPathBase):
    def __init__(self, identifier='*', parent=None):
        self.identifier = identifier
        super(Node, self).__init__(parent=parent)

    @property
    def text(self):
        return Text(parent=self)

    def render_object(self, child=None):
        # Separate nodes from each other
        # TODO: simpler way to do this
        if child and isinstance(child, NodeBase):
            return self.identifier + '/'
        else:
            return self.identifier

    def where(self, *conditions):
        return Where(*conditions, parent=self)


class Text(NodeBase, ComparisonMixin):
    def render_object(self, child=None):
        return 'text()'

    @property
    def normalized(self):
        return NormalizedText(parent=self)


class NormalizedText(Text, ComparisonMixin):
    def __init__(self, parent):
        super(NormalizedText, self).__init__(parent=parent)

    def render(self, child=None):
        return 'normalize-space({path})'.format(path=self._parent.render())
