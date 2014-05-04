from xpath_dsl.base import XPathBase
from xpath_dsl.mixins import RelativeNavigationMixin


class Where(XPathBase, RelativeNavigationMixin):
    def __init__(self, *conditions, **kwargs):
        # kwargs used to preserve order of arguments
        parent = kwargs.pop('parent', None)
        self.conditions = conditions
        super(Where, self).__init__(parent=parent)

    def render_object(self):
        condition_xpath = ' and '.join(condition.render() for condition in self.conditions)
        return '[{condition_xpath}]'.format(condition_xpath=condition_xpath)
