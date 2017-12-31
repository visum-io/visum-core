import unittest
from scripts.github_reader import read_repositories


class TestGithubReader(unittest.TestCase):
    def test_read_repositories(self):
        names = read_repositories()
        self.assertEqual(len(names), 100)


if __name__ == '__main__':
    unittest.main()
