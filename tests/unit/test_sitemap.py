from generate_sitemap import create_sitemap

def test_sitemap_is_updated():
    with open('dash_docs/assets/sitemap.xml', 'r') as f:
        saved_sitemap = f.read()
    assert create_sitemap() == saved_sitemap
