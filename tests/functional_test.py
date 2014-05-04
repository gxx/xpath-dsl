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

    def test_select_parent_of_any_node_with_attribute(self):
        xpath = Builder().any.node.where(
            Attribute('someattribute').equals('something')
        ).parent.render()
        xpath | should | equal_to('//*[@someattribute="something"]/..')

    def test_select_input_with_any_attribute_equaling_value(self):
        xpath = Builder().any.node('input').where(Attribute().equals('test')).render()
        xpath | should | equal_to('//input[@*="test"]')

    def test_select_input_descendant_of_label_whose_normalized_text_equals_value(self):
        xpath = Builder().any.node('label').where(
            Builder().current.any.node.text.normalized.equals('This is a label')
        ).descendant('input').render()
        xpath | should | equal_to('//label[normalize-space(.//*/text())="This is a label"]/input')
