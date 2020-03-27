import pytest
import sys
from generate_sidebar_index import generate_sidebar_index

import pytest
import sys

@pytest.mark.skipif(
    sys.version_info < (3, 7),
    reason="skip non-essential, potentially flaky tests"
)
def test_sidebar_index_is_updated():
    with open('SIDEBAR-INDEX.json', 'r') as f:
        saved_sidebar_index = f.read()
    # if this fails, run $ python generate_sidebar_index.py to update
    assert generate_sidebar_index() == saved_sidebar_index
