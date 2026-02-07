import unittest
import os

class TestRepoStructure(unittest.TestCase):
    def test_root_files_exist(self):
        """Check if critical root files exist."""
        files = ['README.md', 'index.html', 'LICENSE', 'Makefile', 'start-web.sh']
        for f in files:
            self.assertTrue(os.path.exists(f), f"Missing root file: {f}")

    def test_directory_tree(self):
        """Check if critical folders exist."""
        dirs = ['src', 'data', 'tests', 'docs', 'assets', '.github', '.vscode']
        for d in dirs:
            self.assertTrue(os.path.isdir(d), f"Missing directory: {d}")

    def test_asset_placeholders(self):
        """Check if asset folder structure is correct."""
        self.assertTrue(os.path.isdir('assets/images'), "Missing assets/images")
        self.assertTrue(os.path.isdir('assets/colors'), "Missing assets/colors")

    def test_data_integrity(self):
        """Check if data files are in the data folder."""
        self.assertTrue(os.path.exists('data/master_category_bank.json'), "Missing master bank")
        self.assertTrue(os.path.exists('data/categories.json'), "Missing categories.json")
