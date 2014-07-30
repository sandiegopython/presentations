from setuptools import setup, find_packages

requirements = [
    'Django>=1.6,<1.7'
]

development_requirements = [
    'pytest-django==2.6.2',
    'factory-boy==2.4.1',
    'tox==1.6.1',
    'hieroglyph==0.6.5',
]

setup(name='fbp',
      version='0.1.0',
      description='factory boy presentation demo',
      author='Paul Collins',
      author_email='',
      license='MIT',
      install_requires=requirements,
      extras_require={
          'dev': development_requirements,
      },
      packages=find_packages('src'),
      package_dir={'': 'src'},
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
      )
