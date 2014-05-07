from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import AnyNodeOrSpecifiedMixin
from xpath_dsl.mixins import ConditionalMixin
from xpath_dsl.node import Node


# TODO: separate location base Axes from non-location based ones (i.e. attributes are not nodes)
class AxisBase(XPathBase, AnyNodeOrSpecifiedMixin, ConditionalMixin):
    AXIS_JOINER = '::'

    axis_name = None

    def __new__(cls, *args, **kwargs):
        assert cls.axis_name, 'Must override axis_name in inherited classes'
        return super(AxisBase, cls).__new__(cls, *args, **kwargs)

    def __init__(self, parent=None):
        super(AxisBase, self).__init__(parent=parent)

    def render_object(self, child=None):
        # TODO: make this work for all, abstract to some sort of join method
        rendered_text =  self.axis_name + self.AXIS_JOINER
        if not isinstance(child, Node):
            rendered_text += '*'

        return rendered_text


class Ancestor(AxisBase):
    axis_name = 'ancestor'


class AncestorOrSelf(AxisBase):
    axis_name = 'ancestor-or-self'


class Child(AxisBase):
    axis_name = 'child'


class Attribute(AxisBase):
    axis_name = 'attribute'


# TODO: uncomment this, allow as axis, and ensure non-conflict with shortcuts
# class Descendant(AxisBase):
#     axis_name = 'descendant'


class DescendantOrSelf(AxisBase):
    axis_name = 'descendant-or-self'


class Following(AxisBase):
    axis_name = 'following'


class FollowingSibling(AxisBase):
    axis_name = 'follow-sibling'


class Namespace(AxisBase):
    axis_name = 'namespace'


# TODO: same as above
# class Parent(AxisBase):
#     axis_name = 'parent'


class Preceding(AxisBase):
    axis_name = 'preceding'


class PrecedingSibling(AxisBase):
    axis_name = 'preceding-sibling'


class Self(AxisBase):
    axis_name = 'self'
