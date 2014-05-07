from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import RelativeNavigationMixin


class Where(XPathBase, RelativeNavigationMixin):
    def __init__(self, *conditions, **kwargs):
        # kwargs used to preserve order of arguments
        parent = kwargs.pop('parent', None)
        self.conditions = conditions
        super(Where, self).__init__(parent=parent)

    def render_object(self, child=None):
        condition_xpath = ' and '.join(condition.render() for condition in self.conditions)
        return '[{condition_xpath}]'.format(condition_xpath=condition_xpath)

    def where(self, *conditions):
        # It is possible to chain predicates
        return Where(*conditions, parent=self)


class Or(XPathBase):
    def __init__(self, *nodes, **kwargs):
        # kwargs used to preserve order of arguments
        parent = kwargs.pop('parent', None)
        self.nodes = nodes
        super(Or, self).__init__(parent=parent)

    def render_object(self, child=None):
        return '|'.join(node.render() for node in self.nodes)
