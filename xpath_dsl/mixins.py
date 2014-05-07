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


class NavigationMixin(BaseNavigationMixin):
    @property
    def root(self):
        return Root(parent=self)


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


from xpath_dsl.comparison import Equals
from xpath_dsl.conditional import Where
from xpath_dsl.node import Descendant
from xpath_dsl.path import Any
from xpath_dsl.path import Current
from xpath_dsl.path import Parent
from xpath_dsl.path import Root
