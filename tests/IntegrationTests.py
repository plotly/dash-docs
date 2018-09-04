from __future__ import absolute_import
import multiprocessing
import time
import unittest
import percy
from selenium import webdriver
import sys


class IntegrationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(IntegrationTests, cls).setUpClass()

        cls.driver = webdriver.Chrome()

        python_version = sys.version.split(' ')[0]
        if '2.7' in python_version:
            loader = percy.ResourceLoader(webdriver=cls.driver)
            cls.percy_runner = percy.Runner(loader=loader)
            cls.percy_runner.initialize_build()

    @classmethod
    def tearDownClass(cls):
        super(IntegrationTests, cls).tearDownClass()
        cls.driver.quit()
        python_version = sys.version.split(' ')[0]
        if '2.7' in python_version:
            cls.percy_runner.finalize_build()

    def setUp(self):
        pass

    def tearDown(self):
        self.server_process.terminate()

    def startServer(self, app, path='/'):
        def run():
            # Use CDN so that we don't have to reconfigure percy to find the
            # component assets
            app.css.config.serve_locally = False
            app.scripts.config.serve_locally = False
            app.run_server(
                port=8050,
                debug=False,
                processes=4,
                threaded=False
            )

        # Run on a separate process so that it doesn't block
        self.server_process = multiprocessing.Process(target=run)
        self.server_process.start()
        time.sleep(5)

        # Visit the dash page
        self.driver.get('http://localhost:8050{}'.format(path))
        time.sleep(0.5)

        # Inject an error and warning logger
        logger = '''
        window.tests = {};
        window.tests.console = {error: [], warn: [], log: []};

        var _log = console.log;
        var _warn = console.warn;
        var _error = console.error;

        console.log = function() {
            window.tests.console.log.push({method: 'log', arguments: arguments});
            return _log.apply(console, arguments);
        };

        console.warn = function() {
            window.tests.console.warn.push({method: 'warn', arguments: arguments});
            return _warn.apply(console, arguments);
        };

        console.error = function() {
            window.tests.console.error.push({method: 'error', arguments: arguments});
            return _error.apply(console, arguments);
        };
        '''
        self.driver.execute_script(logger)
