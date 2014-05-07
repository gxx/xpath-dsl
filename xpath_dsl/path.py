from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import RelativeNavigationMixin
from xpath_dsl.node import Node


class LazyNode(XPathBase):
    """Allows a node its default, and changes this if called with arguments"""
    def __init__(self, identifier='*', parent=None):
        self.identifier = identifier
        super(LazyNode, self).__init__(parent=parent)

    def __call__(self, identifier='*'):
        return Node(identifier, parent=self._parent)

    def __getattr__(self, item):
        # No need to store state, there is no need for being able to build from top to bottom
        # since building the query is performed bottom to top.
        node = Node(self.identifier, parent=self._parent)
        return getattr(node, item)


class Path(XPathBase):
    @property
    def node(self):
        return LazyNode(parent=self)


class Root(Path):
    def render_object(self, child=None):
        return '/'


class Any(Path):
    def render_object(self, child=None):
        return '//'


class Current(Path, RelativeNavigationMixin):
    def render_object(self, child=None):
        # TODO: determine if always relative?
        if self._parent:
            return '/.'
        else:
            return '.'


class Parent(Path, RelativeNavigationMixin):
    def render_object(self, child=None):
        # TODO: same as determine on relative as above
        if self._parent:
            return '/..'
        else:
            return '..'
