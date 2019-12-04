# pip install git+https://github.com/shadhini/py_pckg_tut.git
# pip uninstall example_package_sapm

from example_package.logger import logger


for i in range(10):
    logger.info('count: {}'.format(i))
