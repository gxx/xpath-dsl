from xpath_dsl.base import XPathBase


class Equals(XPathBase):
    def __init__(self, value, parent):
        self.value = value
        super(Equals, self).__init__(parent=parent)

    def render_object(self, child=None):
        try:
            return '={value}'.format(value=self.value.render())
        except AttributeError:
            return '="{value}"'.format(value=self.value)
