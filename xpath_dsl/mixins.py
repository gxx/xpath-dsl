from xpath_dsl.base import XPathBase


class BaseNavigationMixin(object):
    @property
    def any(self):
        return Any(parent=self)

    @property
    def current(self):
        return Current(parent=self)

    @property
    def parent(self):
        return Parent(parent=self)


class RelativeNavigationMixin(BaseNavigationMixin):
    def descendant(self, identifier):
        return Descendant(identifier, parent=self)


# TODO: add other comparison operators
class ComparisonMixin(object):
    def equals(self, value):
        return Equals(value, parent=self)


class ConditionalMixin(object):
    def where(self, *conditions):
        # It is possible to chain predicates
        return Where(*conditions, parent=self)


class LazyNode(XPathBase):
    """Allows a node its default, and changes this if called with arguments"""
    def __init__(self, identifier='*', parent=None):
        self.identifier = identifier
        super(LazyNode, self).__init__(parent=parent)

    def __call__(self, identifier='*'):
        return Node(identifier, parent=self.parent_node)

    def __getattr__(self, item):
        # No need to store state, there is no need for being able to build from top to bottom
        # since building the query is performed bottom to top.
        node = Node(self.identifier, parent=self.parent_node)
        return getattr(node, item)


class AnyNodeOrSpecifiedMixin(object):
    @property
    def node(self):
        return LazyNode(parent=self)


from xpath_dsl.comparison import Equals
from xpath_dsl.conditional import Where
from xpath_dsl.node import Node
from xpath_dsl.node import Descendant
from xpath_dsl.path import Any
from xpath_dsl.path import Current
from xpath_dsl.path import Parent
