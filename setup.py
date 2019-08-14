from setuptools import setup, find_packages

setup(
    name='ifttt_webhook',
    version='0.1.0',
    description='A Python module to trigger IFTTT events using webhooks.',
    author='Julien de la Bruère-Terreault',
    author_email='drgfreeman@tuta.io',
    url='https://github.com/DrGFreeman/IFTTT-Webhook',
    license='MIT',
    python_requires='>=3.6',
    install_requires=['requests'],
    packages=find_packages(),
)