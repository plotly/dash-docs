import os
from itertools import groupby
import pytest
from dash.testing.browser import Browser
from dash.testing.application_runners import ProcessRunner
from dash_docs.chapter_index import URLS, URL_TO_CONTENT_MAP


@pytest.fixture(scope="session")
def doc_server():
    with ProcessRunner() as server:
        server(raw_command="python index.py", port=8060, start_timeout=60)
        yield server


@pytest.fixture
def dash_doc(doc_server, request):
    with Browser(
        browser=request.config.getoption("webdriver"),
        remote=request.config.getoption("remote"),
        remote_url=request.config.getoption("remote_url"),
        headless=request.config.getoption("headless"),
        options=request.config.hook.pytest_setup_options(),
        percy_assets_root=os.path.join(
            os.path.dirname(__file__), "..", "..", "dash_docs", "assets"
        ),
        percy_finalize=request.config.getoption("nopercyfinalize"),
    ) as browser:
        browser.server_url = doc_server.url
        browser.wait_for_element("#wait-for-layout")
        browser.wait_for_element(".toc .toc--chapter-content")
        yield browser


SNAPSHOT_EXCEPTIONS = {"/dash-bio", "/external-resources", "/search", "/gallery"}


@pytest.fixture(scope="session")
def index_pages():
    yield [
        path
        for path in URL_TO_CONTENT_MAP
        if path not in SNAPSHOT_EXCEPTIONS
    ]
