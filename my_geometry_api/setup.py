from setuptools import setup, find_packages

setup(
    name='my_geometry_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Artem',
    author_email='2015.kurlychkin@mail.ru',
    description='Библиотека для вычисления площади различных фигур',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Hanger12/Python_API_Calculator_Shapes.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)