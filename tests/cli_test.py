import io
import os
import shutil
import sys
import unittest
from contextlib import redirect_stdout
from gitkeep.main import main


class TestCli(unittest.TestCase):
    def setUp(self):
        os.mkdir('test')

    def test_gitkeep_file_creation(self):
        sys.argv[1:] = ['test']
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertTrue(os.path.exists('test/.gitkeep'))

    def tearDown(self):
        shutil.rmtree('test')

if __name__ == '__main__':
    unittest.main()
