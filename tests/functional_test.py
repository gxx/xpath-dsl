from unittest import TestCase

from should_dsl import should

from xpath_dsl import Attribute
from xpath_dsl import Builder


class FunctionalTestCase(TestCase):
    def test_select_root_node(self):
        xpath = Builder().root.node('div').render()
        xpath | should | equal_to('/div')

    def test_select_any_node(self):
        xpath = Builder().any.node('label').render()
        xpath | should | equal_to('//label')

    def test_select_any_node_with_attribute(self):
        xpath = Builder().any.node.where(
            Attribute('someattribute').equals('something')
        ).parent.render()
        xpath | should | equal_to('//*[@someattribute="something"]/..')
