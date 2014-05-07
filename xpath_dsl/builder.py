from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import NavigationMixin
from xpath_dsl.path import Any
from xpath_dsl.path import Current
from xpath_dsl.path import Parent
from xpath_dsl.path import Root


class Builder(XPathBase, NavigationMixin):
    def __init__(self):
        super(Builder, self).__init__(parent=None)

    def render_object(self, child=None):
        return ''

    @property
    def any(self):
        return Any()

    @property
    def current(self):
        return Current()

    @property
    def parent(self):
        return Parent()

    @property
    def root(self):
        return Root()
