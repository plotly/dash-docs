import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_sitemap_is_updated():
    from generate_sitemap import create_sitemap
    with open('dash_docs/assets/sitemap.xml', 'r') as f:
        saved_sitemap = f.read()
    assert create_sitemap() == saved_sitemap
