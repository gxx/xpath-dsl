from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import ComparisonMixin
from xpath_dsl.mixins import ConditionalMixin
from xpath_dsl.mixins import RelativeNavigationMixin


class NodeBase(XPathBase):
    pass


class Node(XPathBase, RelativeNavigationMixin, ConditionalMixin):
    def __init__(self, identifier='*', parent=None):
        self.identifier = identifier
        super(Node, self).__init__(parent=parent)

    @property
    def text(self):
        return Text(parent=self)

    def get_identifier(self):
        return self.identifier

    def render_object(self, child=None):
        # Separate nodes from each other
        # TODO: simpler way to do this
        if child and isinstance(child, NodeBase):
            xpath = self.get_identifier() + '/'
        else:
            xpath = self.get_identifier()

        # TODO: simpler way to do this, too
        # If we are joining a node to a path,
        if (
                self._parent
                and isinstance(self._parent, Path)
                and not self._parent.render_object(child=self).endswith('/')
        ):
            xpath = '/' + xpath

        return xpath


class Descendant(Node, RelativeNavigationMixin, ConditionalMixin):
    def get_identifier(self):
        return '/{identifier}'.format(identifier=self.identifier)


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


from xpath_dsl.path import Path
