from setuptools import setup, find_packages

setup(
    name='transmitter',
    version='0.1.3',
    packages=[
        'transmitter',
        'transmitter.pricefeed',
        'transmitter.pricefeed.adapters',
    ],
    url='http://github.com/emrebeylerhive/transmitter',
    license='MIT',
    author='emrebeylerhive',
    author_email='emrebeylerhive@proton.me',
    description='STEEM Witness updates made easy.',
    entry_points={
        'console_scripts': [
            'transmitter = transmitter.main:main',
        ],
    },
    install_requires=["beem==0.20.12", "requests"]
)