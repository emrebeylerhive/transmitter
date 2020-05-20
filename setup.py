from setuptools import setup

setup(
    name='transmitter',
    version='0.2.7',
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
    install_requires=["beem==0.23.9", "requests", "numpy"]
)
