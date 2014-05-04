class NavigationMixin(object):
    @property
    def root(self):
        return Root(parent=self)

    @property
    def any(self):
        return Any(parent=self)


class RelativeNavigationMixin(object):
    @property
    def any(self):
        return Any(parent=self)

    @property
    def current(self):
        return Current(parent=self)

    @property
    def parent(self):
        return Parent(parent=self)


from xpath_dsl.path import Any
from xpath_dsl.path import Current
from xpath_dsl.path import Parent
from xpath_dsl.path import Root
