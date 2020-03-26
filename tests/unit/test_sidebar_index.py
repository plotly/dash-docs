import pytest
import sys
from generate_sidebar_index import generate_sidebar_index

@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_sidebar_index_is_updated():
    with open('SIDEBAR-INDEX.json', 'r') as f:
        saved_sidebar_index = f.read()
    # if this fails, run $ python generate_sidebar_index.py to update
    assert generate_sidebar_index() == saved_sidebar_index
