from time import sleep
import logging
import pytest
import sys

from dash.testing.wait import until

from dash_docs.chapter_index import URL_TO_CONTENT_MAP

logger = logging.getLogger(__name__)


@pytest.mark.skipif(
    sys.version_info < (3, 0),
    reason="Python 2.7's dev flask server is timing out on many pages now"
)
def test_snap001_index_page_links(dash_doc, index_pages):
    dash_doc.wait_for_element(".toc .toc--chapter-content")
    dash_doc.percy_snapshot("index - 1")
    bad_links = []
    timeout_pages = []

    good_links = ['/', '/search']

    for resource in index_pages:
        if resource.startswith('/'):
            hook_id = "wait-for-page-{}".format(resource)
            res = resource.lstrip("/")
            try:
                dash_doc.driver.get(
                    "{}/{}".format(dash_doc.server_url.rstrip("/"), res)
                )
                dash_doc.wait_for_element_by_id(hook_id)

                if res in ['basic-callbacks', 'datatable/callbacks']:
                    # these two pages have an intermittent problem with their
                    # resource queues not clearing properly. While we sort this out,
                    # just wait a reasonably long time on these pages.
                    sleep(3)
                else:
                    # everything else we can just wait for all callbacks to finish
                    sleep(1)
                    until(dash_doc._wait_for_callbacks, timeout=40, poll=0.3)

                # hide non-repeatable elements before the snapshot
                selectors_to_hide = ",".join([
                    "#my-dashbio-molecule2d",
                    "#molecule2d-selectedatomids",
                    "#molecule2d-modeldata",
                    ".forna-container",
                    "#first_output_3",
                    "#second_output_3",
                    "#third_output_3"
                ])
                dash_doc.driver.execute_script(
                    "document.querySelectorAll('" +
                    selectors_to_hide +
                    "').forEach(el=>el.style.visibility = 'hidden');"
                )
                dash_doc.percy_snapshot(res, wait_for_callbacks=False)
            except Exception as e:
                timeout_pages.append('{} --- on page {}'.format(
                    str(e), resource
                ))

            linked_paths = dash_doc.driver.execute_script(
                'return Array.from(document.querySelectorAll(\'a[href^="/"]\'))'
                '.map(a=>a.attributes.href.value)'
            )
            for link in linked_paths:
                if (link.rstrip('/') not in URL_TO_CONTENT_MAP and
                        link not in good_links and
                        '.mp4' not in link):  # we link to a video on the devtools page
                    msg = '{} --- on page {}'.format(link, resource)
                    logger.info(msg)
                    bad_links.append(msg)

            try:
                dash_doc.driver.execute_script("window.history.go(-1)")
            except Exception as e:
                raise Exception([
                    Exception(['Error going back while on page ', resource]),
                    e
                ])

    assert (bad_links + timeout_pages) == []


def test_snap002_external_resources(dash_doc):
    driver = dash_doc.driver
    resource = "/external-resources"
    driver.get(dash_doc.server_url + resource)
    dash_doc.wait_for_element_by_id("wait-for-page-{}".format(resource))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    dash_doc.percy_snapshot(resource)


def test_snap003_search(dash_doc):
    dash_doc.driver.get(dash_doc.server_url)
    dash_doc.wait_for_element_by_id("sidebar-search-input")
    dash_doc.percy_snapshot("search-blank")
    search = dash_doc.find_element("#sidebar-search-input")
    dash_doc.clear_input(search)
    search.send_keys("dcc.Dropdown")
    dash_doc.wait_for_element(".search-results")
    dash_doc.percy_snapshot("search-dropdown")
