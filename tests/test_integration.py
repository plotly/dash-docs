# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash
from dash.dependencies import Input, Output

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urlparse import urlparse
import base64
import importlib
import io
import multiprocessing
import os
import pandas as pd
import percy
import sys
import time
import unittest

from .IntegrationTests import IntegrationTests
from .utils import assert_clean_console, invincible, wait_for
from tutorial.run import app

# Download geckodriver: https://github.com/mozilla/geckodriver/releases
# And add to path:
# export PATH=$PATH:/Users/chriddyp/Repos/dash-stuff/dash-integration-tests
#
# Uses percy.io for automated screenshot tests
# export PERCY_PROJECT=plotly/dash-integration-tests
# export PERCY_TOKEN=...


class Tests(IntegrationTests):
    def setUp(self):
        def wait_for_element_by_id(id):

            def find_element_by_id():
                try:
                    return self.driver.find_element_by_id(id)
                except:
                    return False
            wait_for(find_element_by_id)
            find_element_by_id()
        self.wait_for_element_by_id = wait_for_element_by_id

        def wait_for_element_by_css_selector(css_selector):
            wait_for(lambda: None is not invincible(
                lambda: self.driver.find_element_by_css_selector(css_selector)
            ))
            return self.driver.find_element_by_css_selector(css_selector)
        self.wait_for_element_by_css_selector = (
            wait_for_element_by_css_selector
        )

    def snapshot(self, name):
        if 'PERCY_PROJECT' in os.environ and 'PERCY_TOKEN' in os.environ:
            python_version = sys.version.split(' ')[0]
            print('Percy Snapshot {}'.format(python_version))
            self.percy_runner.snapshot(name=name)

    def test_docs(self):
        self.startServer(app, '/dash/')

        try:
            self.wait_for_element_by_id('wait-for-layout')
        except Exception as e:
            print(self.wait_for_element_by_id(
                '_dash-app-content').get_attribute('innerHTML'))
            raise e

        self.snapshot('index - 1')

        links = [
            a.get_property('id') for a in
            self.driver.find_elements_by_css_selector('a')
        ]

        def visit_and_snapshot(href):
            self.driver.get('http://localhost:8050{}'.format(href))
            self.wait_for_element_by_id(
                'wait-for-page-{}'.format(href),
                get_message=lambda: 'not found: wait-for-page-{}'.format(href)
            )
            time.sleep(5)
            self.snapshot(href)
            self.driver.back()

        for link in links:
            if link.startswith('/'):
                visit_and_snapshot(link)
