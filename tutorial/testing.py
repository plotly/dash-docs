import dash_html_components as html
import dash_core_components as dcc

logs = '''
14:05:41 | DEBUG | selenium.webdriver.remote.remote_connection:388 | DELETE http://127.0.0.1:53672/session/87b6f1ed3710173eff8037447e2b8f56 {"sessionId": "87b6f1ed3710173eff8037447e2b8f56"}
14:05:41 | DEBUG | urllib3.connectionpool:393 | http://127.0.0.1:53672 "DELETE /session/87b6f1ed3710173eff8037447e2b8f56 HTTP/1.1" 200 72
14:05:41 | DEBUG | selenium.webdriver.remote.remote_connection:440 | Finished Request
14:05:41 | INFO | dash.testing.application_runners:80 | killing the app runner
14:05:41 | DEBUG | urllib3.connectionpool:205 | Starting new HTTP connection (1): localhost:8050
14:05:41 | DEBUG | urllib3.connectionpool:393 | http://localhost:8050 "GET /_stop-3ef0e64e8688436caced44e9f39d4263 HTTP/1.1" 200 29
'''

layout = html.Div([
    dcc.Markdown(u"""
    # Dash Testing

    *New in Dash v1.0*

    `dash.testing` \U0001f9ea provides some off-the-rack
    `pytest` [fixtures](https://docs.pytest.org/en/latest/fixture.html)
    and a minimal set of testing **APIs** with our internal crafted
    best practices at the integration level.

    This tutorial does not intend to cover the usage of
    [pytest](https://docs.pytest.org/en/latest/) and
    [Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/),
    but focuses on how to do a simple integration test with Dash by hosting
    the App server locally and using a Selenium WebDriver to simulate
    the interaction inside a web browser.

    ![demo](https://user-images.githubusercontent.com/1394467/59383731-83c13480-8d2e-11e9-8866-4ffdcd3b1b45.gif)

    ## Install

    The Dash testing is now part of the main Dash package. After
    `pip install dash`, the Dash `pytest` fixtures are available, you just
    need to install the WebDrivers and you are ready to test.

    - [Chrome Driver](http://chromedriver.chromium.org/getting-started)
    - [Firefox Gecko Driver](https://github.com/mozilla/geckodriver/releases)

    FYI, We run Dash integration tests with Chrome WebDriver.
    But the fixture allows you to choose another browser from the command line,
    e.g. `pytest --webdriver Firefox -k bsly001`.

    **Notes**:

    * The *Gecko(Marionette)* driver from Mozilla is not fully compatible with
    Selenium specifications. Some features may not work as expected.

    * We only include *Chrome* and *Firefox* in the supported list for now,
    but other popular webdrivers may be included based on popular demand.

    ## Example

    ```python
    # 1. imports of your dash app
    import dash
    import dash_html_components as html


    # 2. give each testcase a tcid, and pass the fixture
    # as a function argument, less boilerplate
    def test_bsly001_falsy_child(dash_duo):

        # 3. define your app inside the test function
        app = dash.Dash(__name__)
        app.layout = html.Div(id="nully-wrapper", children=0)

        # 4. host the app locally in a thread, all dash server configs could be
        # passed after the first app argument
        dash_duo.start_server(app)

        # 5. use wait_for_* if your target element is the result of a callback,
        # keep in mind even the initial rendering can trigger callbacks
        dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)

        # 6. use this form if its present is expected at the action point
        assert dash_duo.find_element("#nully-wrapper").text == "0"

        # 7. to make the checkpoint more readable, you can describe the
        # acceptance criterion as an assert message after the comma.
        assert dash_duo.get_logs() == [], "browser console should contain no error"

        # 8. visual testing with percy snapshot
        dash_duo.percy_snapshot("bsly001-layout")
    ```

    Notes

    * #1 For most test scenarios, you don't need to import any modules for
    the test; just import what you need for the Dash app itself.

    * #2 A test case is a regular Python function. The function name follows
    this pattern: `test_{tcid}_{test title}`. The `tcid` (test case ID) is
    an abbreviation pattern of `mmffddd => module + file + three digits`.
    The `tcid` facilitates the test selection by just running
    `pytest -k {tcid}`. Its naming convention also helps code navigation with
    modern editors.

    * #3 Here we just define our app inside a test function. All the rules
    still apply as in your app file.

    * #4 We normally start the test by calling the `start_server` API
    from `dash_duo` (you can use `dash_br` for an hosted Dash App, and
    write `dash_br.server_url = "Hosted URL"` to start). Several actions
    implicitly happen under the hood:

        1. The defined app is hosted inside a light Python `threading.Thread`.
        2. A Selenium WebDriver is initialized and navigates to the
        local server URL using `server_url`.
        3. We first wait until the Flask server is responsive to an HTTP
        request; and then make sure the Dash app is full rendered inside
        the browser.

    * #5 A test case is composed of preparation, actions, and checkpoints.
    Both #5 and #6 are doing the same check in this example; we are expecting
    that the defined `Div` component's text is identical to `children`. #5 will
    wait for the expected state to be reached within a 4 seconds timeout. It's
    a safer way to write the action steps when you are doing an element check
    related to callbacks, as it normally happens under Dash context:
    the element is already present in the DOM, but not necessarily the props.

    * #6 The `find_element` API call has an implicitly global timeout of two
    seconds set at the driver level, i.e. the driver waits at most two seconds
    to find the element by the locator, **HOWEVER** it will compare the text
    as soon as the driver returns an element. Also note that the API
    `find_element('#nully-wrapper')` is just a shortcut to a more tedious
    version `driver.find_element_by_css_selector('#nully-wrapper')`.

    * #7 Unlike `unittest`, `pytest` allows using the standard Python
    [`assert`](https://docs.pytest.org/en/latest/assert.html) for verifying
    expectations and values. It also puts more introspection information into
    the assertion failure message by overriding the `assert` behavior. It's
    good practice to expose your *acceptance criteria* directly in the test
    case rather than wrapping the `assert` inside another helper API, also to
    write these messages with SHOULD/SHOULD NOT without failure confusion.
    By looking at the test name, the app definition, the acitons, and the
    checkpoints, reviewers should figure out easily the purpose of the test.

    * #8 We use [Percy](https://percy.io/) as our Visual Regression Testing
    tool. It's a good alternative to assertions when your checkpoint is
    about the graphical aspects of a Dash App, such as the whole layout or a
    `dcc.Graph` component. We integrate the Percy service with a `PERCY_TOKEN`
    variable, so the regression result is only available in Plotly's CircleCI
    setup.

    ## Fixtures

    To avoid accidental name collision with other pytest plugins,
    all Dash test fixtures start with the prefix `dash_`.

    - dash_duo

    The default fixture for Dash integration tests, it contains a
    `thread_server` and a WebDriver wrapped with high-level Dash testing APIs.

    - dash_br

    A standalone WebDriver wrapped with high-level Dash testing APIs. This is
    suitable for testing a Dash App in a deployed environment, i.e. when
    your Dash App is accessible from a URL.

    - dash_thread_server

    Start your Dash App locally in a Python `threading.Thread`, which is
    lighter and faster than a process.

    - dash_process_server

    Start your Dash App with `waitress` in a Python `subprocess`. This is
    close to your production/deployed environment.  **Note:**  *You need to
    configure your `PYTHONPATH` so that the Dash app source file is
    directly importable*.

    ## APIs

    ### Selenium Overview

    Both `dash_duo` and `dash_br` expose the Selenium WebDriver via the
    property `driver`, e.g. `dash_duo.driver`, which gives you full access to
    the [Python Selenium API](https://selenium-python.readthedocs.io/api.html).
    (*Note that this is not the official Selenium documentation site, but has
    somehow become the defacto Python community reference*)

    One of the core components of selenium testing is finding the
    **web element** with a `locator`, and performing some actions like `click`
    or `send_keys` on it, and waiting to verify if the expected state is met
    after those actions. The check is considered as an acceptance criterion,
    for which you can write in a standard Python `assert` statement.

    #### Element Locators

    There are several strategies to
    [locate elements](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements);
    CSS selector and XPATH are the two most versatile ways. We recommend using
    the **CSS Selector** in most cases due to its
    [better performance and robustness](http://elementalselenium.com/tips/34-xpath-vs-css-revisited-2) across browsers.

    If you are new to using CSS Selectors, these
    [SauceLab tips](https://saucelabs.com/resources/articles/selenium-tips-css-selectors)
    are a great start. Also, remember that
    [Chrome Dev Tools Console](https://developers.google.com/web/tools/chrome-devtools/console/utilities)
    is always your good friend and playground.

    ![dev tools](https://user-images.githubusercontent.com/1394467/59371148-3505a180-8d12-11e9-9ad6-7dce223b6019.png)

    #### Waits

    [This link](https://selenium-python.readthedocs.io/waits.html) covers
    this topic nicely. For impatient readers, a quick take away is
    quoted as follows:

    The Selenium WebDriver provides two types of waits:

    - **explicit wait**
        Makes WebDriver wait for a certain condition to occur before
        proceeding further with execution. All our APIs with `wait_for_*`
        falls into this category.
    - **implicit wait**
        Makes WebDriver poll the DOM for a certain amount of time when trying
        to locate an element. We set a global two-second timeout at the
        `driver` level.

    **Note** *all custom wait conditions are defined in `dash.testing.wait`
    and there are two extra APIs `until` and `until_not` which are similar to
    the explicit wait with WebDriver, but they are not binding to
    WebDriver context, i.e. they abstract a more generic mechanism to
    poll and wait for certain condition to happen*

    ### Browser APIs

    This section lists a minimal set of Dash testing helper APIs.
    They are convenient shortcuts to Selenium APIs and have been approved in
    our daily integration tests.

    The following table might grow as we start migrating more legacy tests in
    the near future. But we have no intention to build a comprehensive list,
    the goal is to make writing Dash tests concise and error-free.
    Please feel free to submit a community PR to add any missing ingredient,
    we would be happy to accept that if it's adequate for Dash testing.

    | API | Description |
    | --- | ----------- |
    | `find_element(selector)` | return the first found element by the `CSS selector`, shortcut to `driver.find_element_by_css_selector`. *note that this API will raise exceptions if not found, the `find_elements` API returns an empty list instead* |
    | `find_elements(selector)` | return a list of all elements matching by the `CSS selector`, shortcut to `driver.find_elements_by_css_selector`|
    | `multiple_click(selector, clicks)`| find the element with the `CSS selector` and clicks it with number of `clicks` |
    | `wait_for_element(selector, timeout=None)` | shortcut to `wait_for_element_by_css_selector` the long version is kept for back compatibility. `timeout` if not set, equals to the fixture's `wait_timeout`|
    | `wait_for_element_by_css_selector(selector, timeout=None)` | explicit wait until the element to present, shortcut to `WebDriverWait` with `EC.presence_of_element_located` |
    | `wait_for_style_to_equal(selector, style, value, timeout=None)` | explicit wait until the element's style has expected `value`. shortcut to `WebDriverWait` with custom wait condition `style_to_equal`. `timeout` if not set, equals to the fixture's `wait_timeout`  |
    | `wait_for_text_to_equal(selector, text, timeout=None)` | explicit wait until the element's text equals the expected `text`. shortcut to `WebDriverWait` with custom wait condition `text_to_equal`. `timeout` if not set, equals to the fixture's `wait_timeout` |
    | `wait_for_contains_text(selector, text, timeout=None)` | explicit wait until the element's text contains the expected `text`. shortcut to `WebDriverWait` with custom wait condition `contains_text` condition. `timeout` if not set, equals to the fixture's `wait_timeout` |
    | `wait_for_page(url=None, timeout=10)` | navigate to the `url` in webdriver and wait until the dash renderer is loaded in browser. use `server_url` if `url` is None |
    | `toggle_window()` | switch between the current working window and the newly opened one. |
    | `switch_window(idx)` | switch to window by window index. shortcut to `driver.switch_to.window`. raise `BrowserError` if no second window present in browser |
    | `open_new_tab(url=None)` | open a new tab in browser with window name `new window`. `url` if not set, equals to `server_url` |
    | `percy_snapshot(name)` | visual test API shortcut to `percy_runner.snapshot` it also combines the snapshot `name` with python versions |
    | `take_snapshot(name)` | hook method to take a snapshot while selenium test fails. the snapshot is placed under `/tmp/dash_artifacts` in Linux or `%TEMP` in windows with a filename combining test case `name` and the running selenium session id |
    | `get_logs()` | return a list of `SEVERE` level logs after last reset time stamps (default to 0, resettable by `reset_log_timestamp`. **Chrome only** |
    | `clear_input()` | simulate key press to clear the input |
    | `driver` | expose the Selenium WebDriver as fixture property |
    | `session_id` | shortcut to `driver.session_id` |
    | `server_url` | set the server_url as setter so the selenium is aware of the local server port, it also implicitly calls `wait_for_page`. return the server_url as property |


    ## Debugging

    ### Verify your test environment

    If you run the integration in a virtual environment, make sure you are
    getting the latest commit in the **master** branch from each component, and
    that the installed `pip` versions are correct.

    Note: *We have some enhancement initiatives tracking in this [issue](https://github.com/plotly/dash/issues/759)*

    ### Run the CI job locally

    The [CircleCI Local CLI](https://circleci.com/docs/2.0/local-cli/) is a
    handy tool to run all the jobs locally. It gives you an earlier warning
    before even pushing your commits to remote, which leaves no chance of
    making an embarrassing public mistake. The environment is identical to the
    remote one, except the Percy snapshot and test reports are not functional
    locally.

    ```shell
    # install the cli (first time only)
    $ curl -fLSs https://circle.ci/cli | bash && circleci version

    # trigger a local circleci container session
    # you should run at least one python version locally
    # note: the current config requires all tests pass on python 2.7, 3.6 and 3.7.
    $ circleci local execute --job python-3.6
    ```

    ### Increase the verbosity of pytest logging level

    `pytest --log-cli-level DEBUG -k bsly001`

    You can get more logging information from Selenium WebDriver, Flask server,
    and our test APIs.

    ```bash
    14:05:41 | DEBUG | selenium.webdriver.remote.remote_connection:388 | DELETE http://127.0.0.1:53672/session/87b6f1ed3710173eff8037447e2b8f56 {"sessionId": "87b6f1ed3710173eff8037447e2b8f56"}
    14:05:41 | DEBUG | urllib3.connectionpool:393 | http://127.0.0.1:53672 "DELETE /session/87b6f1ed3710173eff8037447e2b8f56 HTTP/1.1" 200 72
    14:05:41 | DEBUG | selenium.webdriver.remote.remote_connection:440 | Finished Request
    14:05:41 | INFO | dash.testing.application_runners:80 | killing the app runner
    14:05:41 | DEBUG | urllib3.connectionpool:205 | Starting new HTTP connection (1): localhost:8050
    14:05:41 | DEBUG | urllib3.connectionpool:393 | http://localhost:8050 "GET /_stop-3ef0e64e8688436caced44e9f39d4263 HTTP/1.1" 200 29
    ```

    ### Selenium Snapshots

    If you run your tests with CircleCI dockers (locally with `CircleCI CLI`
    and/or remotely with `CircleCI`).

    Inside a docker run or VM instance where there is no direct access to the
    video card, there is a known limitation that you cannot see anything from
    the Selenium browser on your screen. Automation developers use
    [Xvfb](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml) as
    a workaround to solve this issue. It enables you to run graphical
    applications without a display (e.g., browser tests on a CI server) while
    also having the ability to take screenshots.

    We implemented an automatic hook at the test report stage, it checks if a
    test case failed with a Selenium test fixture. Before tearing down every
    instance, it will take a snapshot at the moment where your assertion is
    `False` or having a runtime error. refer to [Browser APIs](#browser-apis)

    *Note: you can also check the snapshot directly in CircleCI web page
    under `Artifacts` Tab*

    ![CircleCI](https://user-images.githubusercontent.com/1394467/59371162-3f27a000-8d12-11e9-9060-7d8a8522c2c6.png)
    """),
])
