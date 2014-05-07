from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import ConditionalMixin
from xpath_dsl.mixins import RelativeNavigationMixin
from xpath_dsl.mixins import AnyNodeOrSpecifiedMixin


class Path(XPathBase, AnyNodeOrSpecifiedMixin, ConditionalMixin):
    def render(self, child=None):
        # TODO: refactor this to have a common base with axes
        value = super(Path, self).render()
        if child and not isinstance(child, (Node, Path)):
            value += '*'

        return value


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


from xpath_dsl.node import Node
