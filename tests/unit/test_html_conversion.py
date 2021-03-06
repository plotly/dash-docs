import pytest
import sys
from dash_docs.convert_to_html import convert_to_html

@pytest.mark.skipif(
    sys.version_info < (3, 7),
    reason="skip non-essential, potentially flaky tests"
)
def test_html_conversion():
    exceptions = []
    success = []
    dcc_link = []
    from dash_docs.chapter_index import URL_TO_CONTENT_MAP
    for url in URL_TO_CONTENT_MAP:
        try:
            ssr_content = convert_to_html(URL_TO_CONTENT_MAP[url])
            if '<dccLink' in ssr_content:
                dcc_link.append(url)
            else:
                success.append(url)
        except Exception as e:
            exceptions.append([url, e])

    error_message = ''
    if len(exceptions) > 0:
        for i in exceptions:
            error_message += '\n===============\nIssue with ' + i[0] + '\n' + str(i[1]) + '\n\n\n'

        error_message += '\n\n\nThese URLs were OK:\n{}'.format(
            '-' + '\n-'.join(success)
        )

        error_message += '\n\n\nThese URLs had exceptions:\n{}'.format(
            '-' + '\n-'.join([i[0] for i in exceptions])
        )

        error_message += '\n\n\nThese URLs still had dccLink in their content:\n{}'.format(
            '-' + '\n-'.join(dcc_link)
        )

        error_message += '\n\n{} OK, {} need to be fixed, {} need dccLink fixed'.format(
            len(success), len(exceptions), len(dcc_link))


    assert len(exceptions) == 0 and len(dcc_link) == 0, error_message
