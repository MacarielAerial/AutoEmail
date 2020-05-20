rom distutils.core import setup

setup(
  name = 'AutoEmail',
  packages = ['AutoEmail'],
  version = '0.0.1',
  license='MIT',
  description = 'Send customised emails to a selected list of recipients',
  long_description = long_description,
  author = 'Yifei Yu',
  author_email = 'yyu.mam2020@london.edu',
  url = 'https://github.com/MacarielAerial/AutoEmail',
  download_url = '',
  keywords = ['SALES', 'FORECAST', 'LSTM', 'EMBEDDING'],
  install_requires=[
          'numpy',
          'pandas',
          'matplotlib',
          'sklearn',
          'tensorflow',
          'pydot',
          'graphviz'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
  python_requires = '>= 3.6'
)

