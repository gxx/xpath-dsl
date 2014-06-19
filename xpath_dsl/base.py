class TreeBase(object):
    def add_node(self, node):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()


class TreeChildren(TreeBase):
    def __init__(self):
        self._children = []

    def __len__(self):
        return len(self._children)

    def __iter__(self):
        return iter(self._children)

    def __getitem__(self, item):
        return self._children[item]

    def add_node(self, node):
        self._children.append(node)

    def render(self):
        return ''.join(child.render() for child in self._children)


class TreeNode(TreeBase):
    def __init__(self):
        self.children = TreeChildren()

    def add_node(self, node):
        self.children.add_node(node)

    def render_object(self):
        raise NotImplementedError()

    def render(self):
        return ''.join([self.render_object(), self.children.render()])


class XPathBase(object):
    NODE_JOINER = ''

    def __init__(self):
        self.children = []

    def __repr__(self):
        return '<{class_name}: {info}>'.format(
            class_name=self.__class__.__name__,
            info=str(self)
        )

    def __unicode__(self):
        return unicode(self.render())

    def __str__(self):
        return self.render()

    def __or__(self, other):
        # TODO: fix this
        from xpath_dsl.conditional import Or
        return Or(self, other)

    def add_node(self, node):
        self.children.append(node)

    def render_object(self):
        raise NotImplementedError()

    def render(self):

