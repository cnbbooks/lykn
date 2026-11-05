import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


SCRIPT = Path(__file__).with_name('mdbook-epub-image-paths.py')
SPEC = importlib.util.spec_from_file_location('epub_image_paths', SCRIPT)
epub = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(epub)


class EpubImagePathsTest(unittest.TestCase):
    def test_ebook_cover_uses_existing_small_asset(self):
        source = (SCRIPT.parent.parent / 'src/README.md').read_text()
        result = epub.rewrite_content('README.md', source)
        self.assertIn('[cover-large]: images/cover.png', result)
        self.assertNotIn('images/cover-large.png', result)
        self.assertIn('[cover-large]: images/cover-large.png', source)

    def test_nested_image_paths_still_resolve(self):
        self.assertEqual(
            epub.rewrite_content('part1/chapter2/README.md', '![Chapter](../../images/ch2.png)'),
            '![Chapter](../../images/ch2.png)',
        )

    def test_cover_substitution_covers_inline_and_html_images(self):
        for source, expected in [
            ('![Cover](images/cover-large.png)', '![Cover](images/cover.png)'),
            ('<img src="images/cover-large.png">', '<img src="images/cover.png">'),
        ]:
            with self.subTest(source=source):
                self.assertEqual(epub.rewrite_content('README.md', source), expected)

    def test_external_images_and_fragments_stay_unchanged(self):
        source = '![Cover](https://example.com/cover-large.png)\n[section]: #cover'
        self.assertEqual(epub.rewrite_content('part1/README.md', source), source)

    def test_nested_cover_keeps_its_relative_path(self):
        self.assertEqual(
            epub.rewrite_content('preface/README.md', '[cover]: ../images/cover-large.png'),
            '[cover]: ../images/cover.png',
        )

    def test_only_epub_renderer_is_supported(self):
        self.assertEqual(epub.run_supports_check('epub'), 0)
        self.assertEqual(epub.run_supports_check('html'), 1)

    def test_preprocessor_rewrites_current_and_legacy_book_shapes(self):
        for key in ['items', 'sections']:
            chapter = {
                'path': 'README.md',
                'content': '[cover-large]: images/cover-large.png\n',
                'sub_items': [{
                    'Chapter': {
                        'path': 'part1/chapter2/README.md',
                        'content': '![Chapter](../../images/ch2.png)',
                        'sub_items': [],
                    },
                }],
            }
            with self.subTest(book_key=key):
                result = subprocess.run(
                    [sys.executable, '-B', str(SCRIPT)],
                    input=json.dumps([{'renderer': 'epub'}, {key: [{'Chapter': chapter}]}]),
                    capture_output=True,
                    text=True,
                    check=True,
                )
                actual = json.loads(result.stdout)[key][0]['Chapter']
                self.assertEqual(actual['content'], '[cover-large]: images/cover.png\n')
                self.assertEqual(
                    actual['sub_items'][0]['Chapter']['content'],
                    '![Chapter](../../images/ch2.png)',
                )

    def test_attribution_is_not_an_automatic_redirect(self):
        source = (SCRIPT.parent.parent / 'src/redirects/mdbook.html').read_text()
        self.assertNotIn('http-equiv', source)
        self.assertIn('href="https://github.com/rust-lang/mdbook/"', source)


if __name__ == '__main__':
    unittest.main()
