import setuptools

setuptools.setup(
    name="pennant",
    version="0.1.5",
    packages=['pennant'],
    package_dir={'pennant': 'src'},
    include_package_data=True,
    description="A high-spirited feature-flagging library for Python.",
    long_description="""
=======
pennant
=======

A feature flagging library that uses decorators and context management to "feature flag"
certain functions or blocks of code. I feel like it's better than a bunch of conditionals,
but I'm often wrong.

Notes
=====
Contrary to how some folks might do it, this library takes and "opt-out" approach where
setting the flag to False prevents the given function or code block from running. As long
as the argument provided to the decorator or content manager evaluates to False,
anything's game.
    """,
    long_description_content_type="text/x-rst",
    install_requires=[],
    url="https://github.com/dluman/pennant"
 )
