from dash_docs.reusable_components.Markdown import replace_relative_links
import os
import pytest

@pytest.mark.parametrize(
    "markdown_string, expected_output", [
    [
        '<dccLink href="/test" children="that"/>',
        '<dccLink href="/Docs/test" children="that"/>',
    ],

    [
        '''
        <dccLink href="/test">
            <code>that</that>
        </dccLink>,
        ''',
        '''
        <dccLink href="/Docs/test">
            <code>that</that>
        </dccLink>,
        '''
    ],
])
def test_relative_links(markdown_string, expected_output):
    os.environ['DASH_DOCS_URL_PREFIX'] = '/Docs/'
    try:
        assert replace_relative_links(markdown_string) == expected_output
    except Exception as e:
        os.environ['DASH_DOCS_URL_PREFIX'] = ''
        raise e
    os.environ['DASH_DOCS_URL_PREFIX'] = ''
