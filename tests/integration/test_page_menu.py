import time
import pytest
import sys


@pytest.mark.skipif(
    sys.version_info < (3, 7),
    reason="skip non-essential, potentially flaky tests"
)
def test_page_menu_001(dash_doc):
    dash_doc.driver.get(dash_doc.server_url + '/testing')

    # make window very wide so that pagemenu isn't hidden from media query
    dash_doc.driver.set_window_size(2000, 1000)

    dash_doc.wait_for_element_by_id("page-menu--links")
    testing_links = [
        'Dash Testing',
        'Install',
        'Caveats',
        'Example',
        'Dash for R testing',
        'Fixtures',
        'APIs',
        'Selenium Overview',
        'Element Locators',
        'Waits',
        'Browser APIs',
        'Dash APIs',
        'Debugging',
        'Verify your test environment',
        'Run the CI job locally',
        'Increase the verbosity of pytest logging level',
        'Selenium Snapshots',
        'Percy Snapshots',
    ]

    # Long sleep because the `wait_for_text_to_equal` command
    # was raising "StaleElementReferenceException" exceptions
    # See https://github.com/plotly/dash/issues/1164
    for i in range(len(testing_links)):
        dash_doc.wait_for_text_to_equal(
            '#page-menu--link-{}'.format(i),
            testing_links[i],
        )

    dash_doc.find_element('#logo-home').click()
    dash_doc.wait_for_element_by_id("page-menu--links")

    home_links = [
        'Dash User Guide',
        'What\'s Dash?',
        'Dash Tutorial',
        'Dash Callbacks',
        'Open Source Component Libraries',
        'Creating Your Own Components',
        'Beyond the Basics',
        'Production',
        'Getting Help',
        'Dash Enterprise',
    ]

    for i in range(len(home_links)):
        dash_doc.wait_for_text_to_equal(
            '#page-menu--link-{}'.format(i),
            home_links[i]
        )
