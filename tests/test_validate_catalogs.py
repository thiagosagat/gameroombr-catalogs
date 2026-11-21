import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_catalogs import validate_document


class ValidateDocumentTests(unittest.TestCase):
    def test_accepts_empty_catalog(self):
        errors, count = validate_document("empty.json", {"DATA": {}})
        self.assertEqual(errors, [])
        self.assertEqual(count, 0)

    def test_accepts_valid_direct_pkg_entry(self):
        doc = {
            "DATA": {
                "https://downloads.example.org/tool.pkg": {
                    "name": "Example Tool",
                    "size": 12345,
                    "official_sha256": "a" * 64,
                }
            }
        }
        errors, count = validate_document("apps.json", doc)
        self.assertEqual(errors, [])
        self.assertEqual(count, 1)

    def test_rejects_non_https_url(self):
        doc = {
            "DATA": {
                "http://example.org/tool.pkg": {"name": "Bad", "size": 123}
            }
        }
        errors, _ = validate_document("apps.json", doc)
        self.assertTrue(any("HTTPS" in error for error in errors))

    def test_rejects_https_url_without_pkg_extension(self):
        doc = {
            "DATA": {
                "https://example.org/tool.zip": {"name": "Bad", "size": 123}
            }
        }
        errors, _ = validate_document("apps.json", doc)
        self.assertTrue(any("end in .pkg" in error for error in errors))

    def test_rejects_missing_name_and_invalid_size(self):
        doc = {
            "DATA": {
                "https://example.org/tool.pkg": {"name": "", "size": 0}
            }
        }
        errors, _ = validate_document("apps.json", doc)
        self.assertTrue(any("'name'" in error for error in errors))
        self.assertTrue(any("'size'" in error for error in errors))

    def test_rejects_duplicate_pkg_urls(self):
        seen = {"https://example.org/tool.pkg": "homebrew.json"}
        doc = {
            "DATA": {
                "https://example.org/tool.pkg": {"name": "Tool", "size": 123}
            }
        }
        errors, _ = validate_document("apps.json", doc, seen)
        self.assertTrue(any("duplicate PKG URL" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
