class XPathBase(object):
    def __init__(self, parent=None):
        self._parent = parent

    def __repr__(self):
        return '<{class_name}: {info}>'.format(
            class_name=self.__class__.__name__,
            info=str(self)
        )

    def __unicode__(self):
        return unicode(self.render())

    def __str__(self):
        return self.render()

    def render_object(self):
        raise NotImplementedError()

    def render(self):
        if self._parent:
            return self._parent.render() + self.render_object()
        else:
            return self.render_object()

    def __or__(self, other):
        raise NotImplementedError()
        return Or(self, other)


# from xpath_dsl.builder import Or
