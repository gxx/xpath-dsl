from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import NavigationMixin
from xpath_dsl.path import Current


class Builder(XPathBase, NavigationMixin):
    def __init__(self):
        super(Builder, self).__init__(parent=None)

    def render_object(self, child=None):
        return ''

    @property
    def current(self):
        return Current()
