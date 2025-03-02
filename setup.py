from setuptools import setup, find_packages

setup(
    name='screw-spacing',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'screw-spacing=screw_spacing.main:main',
        ],
    },
    install_requires=[
        'z3-solver',
        'argparse',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='Calculates even hole spacing to lengths of stock, e.g. for attaching rails with screws.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/screw-spacing',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)