#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from links import is_social, primary_link, story_urls
from products import classify_products, parse_product_ids


class ProductTests(unittest.TestCase):
    def test_stringified_list(self):
        self.assertEqual(parse_product_ids('["2","4501"]'), ["2", "4501"])

    def test_crm_is_in_scope(self):
        result = classify_products('["2","4601"]')
        self.assertEqual(result["scope"], "in_scope")
        self.assertIn("CRM", result["in_scope_products"])

    def test_books_is_out(self):
        self.assertEqual(classify_products('["4601"]').get("scope"), "out_of_scope")

    def test_crm_plus_is_a_bundle(self):
        result = classify_products('["180000"]')
        self.assertEqual(result["scope"], "in_scope")
        self.assertTrue(result["bundle"])

    def test_empty_is_unknown(self):
        self.assertEqual(classify_products("[]")["scope"], "unknown")


class LinkTests(unittest.TestCase):
    def test_file_id_wins_over_a_social_testimonial(self):
        link = primary_link("2005432631953", "https://www.facebook.com/reel/1")
        self.assertEqual(link, "zoho-file:2005432631953")

    def test_minus_one_uses_the_testimonial_url(self):
        link = primary_link("-1", "https://www.youtube.com/watch?v=abc")
        self.assertTrue(is_social(link))

    def test_description_url_is_kept(self):
        primary, urls = story_urls({
            "casestudy_link": "2005432631953",
            "testimonial_link": "",
            "casestudy_description": "See https://www.zoho.com/crm/customers/example.html",
        })
        self.assertEqual(primary, "zoho-file:2005432631953")
        self.assertIn("https://www.zoho.com/crm/customers/example.html", urls)


if __name__ == "__main__":
    unittest.main()
