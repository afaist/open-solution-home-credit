from setuptools import setup

setup(
    name='opensolutionhomecredit',
    version='1.2.2',
    description='open-solution-home-credit',
    author='open-solution-home-credit',
    author_email='example@example.com',
    packages=['src'],  #same as name
    package_data={'src': ['kaggle.yaml']},
    install_requires=['neptune-cli','steppy','steppy-toolkit','attrdict','click','swifter','toolz','cloudpickle'],
)
