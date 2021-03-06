from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'AutoEmail',
  packages = ['AutoEmail'],
  version = '0.0.3',
  license='MIT',
  description = 'Send customised emails to a selected list of recipients',
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'Yifei Yu',
  author_email = 'yyu.mam2020@london.edu',
  url = 'https://github.com/MacarielAerial/AutoEmail',
  download_url = 'https://github.com/MacarielAerial/AutoEmail/archive/v_0.0.3.tar.gz',
  keywords = ['AUTOMATION', 'OFFICE', 'MYSQL', 'EMAIL'],
  install_requires=[
          'numpy',
          'pandas',
          'mysql.connector',
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

