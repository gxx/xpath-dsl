# XPath DSL

A programmatic DSL for manipulating XPath queries without actually executing them.
This is useful for things such as creating complex, chainable queries without hard-coding logic. For example, passing a built XPath to Selenium.

# Usages

```python
from xpath_dsl import Builder
from xpath_dsl import Attribute
from xpath_dsl import Text

# Note: When to use builder or objects directly
# Use Builder() when you are building a path. If you are only creating a fragment without
# A full path, then use the objects you need. i.e. inside a where clause without a path

# Creates "/div"
Builder().root.node('div')

# Creates "//label"
Builder().any.node('label')

# Creates "//*[@class="something"]"
Builder().any.node.where(Attribute('class').equals('something'))

# Creates "//*[@someattribute]/..
Builder().any.node.where(Attribute('someattribute')).parent

# Creates "//input[@*="test"]"
Builder().any.node('input').where(Attribute().equals('test'))

# Creates "//label[normalize-space(.//*/text())="This is a label"]/input"
Builder().any.node('label').where(
    Builder().current.any.node.text.normalized.equals('This is a label')
).descendant('input')

# Creates "//label[normalize-space(.//*/text())="This is a label"]/input | //label[normalize-space(text())="This is a label"]/input"
Builder().any.node('label').where(
        Builder().current.any.node.text.normalized.equals('This is a label')
).descendant('input')
| Builder().any.node('label').where(
        Text().normalized.equals('This is a label')
    ).descendant('input')
)
```
