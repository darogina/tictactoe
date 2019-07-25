import glob
import os
import shutil
from distutils.command.clean import clean

from setuptools import setup


class CleanCommand(clean, object):
    """Custom clean command to tidy up the project root."""
    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info'.split(' ')

    def run(self):
        here = os.getcwd()

        # Execute the classic clean command
        super(CleanCommand, self).run()

        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob.glob(os.path.normpath(os.path.join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError("%s is not a path inside %s" % (path, here))
                print('removing %s' % os.path.relpath(path))
                shutil.rmtree(path)


setup(
    name='tic-tac-toe',
    version='0.1',
    description='Tic-Tac-Toe game',
    scripts=['tictactoe.py'],
    url='http://github/darogina/tictactoe/',
    author='David Rogina',
    license='MIT',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'tictactoe = tictactoe:main',
        ],
    },
    cmdclass={'clean': CleanCommand}
)
