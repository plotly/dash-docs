from __future__ import absolute_import
import multiprocessing
import time
import unittest
import logging
import os
import percy
from selenium import webdriver
import sys
import warnings

log = logging.getLogger('werkzeug')
log.disabled = True
warnings.filterwarnings("ignore")


class IntegrationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(IntegrationTests, cls).setUpClass()

        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(2)

        python_version = sys.version.split(' ')[0]
        if '2.7' in python_version:
            root_static_dir = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    '..',
                    'assets'
                )
            )
            loader = percy.ResourceLoader(
                webdriver=cls.driver,
                base_url='/assets',
                root_dir=root_static_dir
            )
            cls.percy_runner = percy.Runner(loader=loader)
            print('>>> initialize_build {}'.format(python_version))
            cls.percy_runner.initialize_build()

    @classmethod
    def tearDownClass(cls):
        super(IntegrationTests, cls).tearDownClass()
        cls.driver.quit()
        python_version = sys.version.split(' ')[0]
        if '2.7' in python_version:
            print('>>> finalize_build {}'.format(python_version))
            cls.percy_runner.finalize_build()

    def setUp(self):
        pass

    def tearDown(self):
        self.server_process.terminate()

    def startServer(self, app, path='/'):
        def run():
            app.server.logger.disabled = True
            app.run_server(
                port=8050,
                processes=4,
                threaded=False,
                debug=True,
                use_reloader=False,
                use_debugger=True,
                dev_tools_hot_reload=False,
                dev_tools_ui=True
            )

        # Run on a separate process so that it doesn't block
        self.server_process = multiprocessing.Process(target=run)
        self.server_process.start()
        time.sleep(2)

        # Visit the dash page
        self.driver.get('http://localhost:8050{}'.format(path))

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
