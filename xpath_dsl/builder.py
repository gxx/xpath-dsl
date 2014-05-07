from xpath_dsl.axes import DescendantOrSelf
from xpath_dsl.base import XPathBase
from xpath_dsl.path import Any
from xpath_dsl.path import Current
from xpath_dsl.path import Parent
from xpath_dsl.path import Root


class Builder(XPathBase):
    # TODO: finalize this list
    FUNC_MAP = {
        'any': Any,
        'descendant_or_self': DescendantOrSelf,
        'current': Current,
        'parent': Parent,
        'root': Root
    }

    def __init__(self):
        super(Builder, self).__init__(parent=None)

    def __getattr__(self, item):
        try:
            # TODO: make this work for functions that take arguments
            return self.FUNC_MAP[item]()
        except KeyError:
            raise AttributeError(item)

    def render_object(self, child=None):
        return ''
