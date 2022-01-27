from setuptools import setup, find_packages
from wordle.__main__ import __version__

setup(
    name="wordle",
    version=__version__,
    author="kr@justfoolingaround",
    author_email="kr.justfoolingaround@gmail.com",
    description="Play wordle offline in your cli!",
    packages=find_packages(),
    url="https://github.com/justfoolingaround/wordle-cli",
    keywords=[
        "wordle",
    ],
    install_requires=[
        "ujson",
        "click",
    ],
    package_data={'wordle': ['assets/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        wordle=wordle.__main__:__wordle_cli__
    """,
)