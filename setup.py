from setuptools import setup


def load_requirements_from_file(path):
    with open(path) as requirements_file:
        requirements = requirements_file.readlines()

    # Strip the last character (\n) and filter empty lines
    return filter(None, map(lambda o: o[:-1], requirements))


setup(
    name='xpath-dsl',
    version='0.0.1',
    author='Andrew Crosio',
    author_email='Andrew.Crosio@gmail.com',
    url='https://github.com/Andrew-Crosio/xpath-dsl',
    license='license info',
    description='XPath DSL',
    long_description='XPath DSL',
    packages=['xpath_dsl'],
    include_package_data=True,
    platforms=['any'],
    classifiers=[
        'Topic :: Internet',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Programming Language :: Python :: 2.7',
    ],
    # TODO: determine if this should be in a requirements.txt
    install_requires=[],
    test_suite='tests',
    tests_require=load_requirements_from_file('devrequirements.txt'),
)
