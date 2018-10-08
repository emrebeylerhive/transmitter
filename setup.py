from setuptools import setup

setup(
    name='witness_transmitter',
    version='0.0.1',
    packages=["transmitter",],
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
    install_requires=["beem", "logme"]
)