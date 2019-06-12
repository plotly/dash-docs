# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
import importlib
import io
import multiprocessing
import os
import pandas as pd
import percy
import sys
import unittest

from .IntegrationTests import IntegrationTests
from .utils import assert_clean_console, invincible, wait_for
from run import app

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
            if '2.7' in python_version:
                print('>>> Percy Snapshot {} - {}'.format(python_version, name))
                self.percy_runner.snapshot(name=name)

    def test_docs(self):
        self.startServer(app, '/')

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
        ] + [
            '/dash-core-components/dropdown',
            '/dash-core-components/slider',
            '/dash-core-components/rangeslider',
            '/dash-core-components/input',
            '/dash-core-components/textarea',
            '/dash-core-components/checklist',
            '/dash-core-components/radioitems',
            '/dash-core-components/datepickersingle',
            '/dash-core-components/datepickerrange',
            '/dash-core-components/markdown',
            '/dash-core-components/upload',
            '/dash-core-components/tabs',
            '/dash-core-components/button'

        ] + [
            '/dash-deployment-server/ssh',
            '/dash-deployment-server/initialize',
            '/dash-deployment-server/application-structure',
            '/dash-deployment-server/static-assets',
            '/dash-deployment-server/deployment',
            '/dash-deployment-server/app-authentication',
            '/dash-deployment-server/privacy',
            '/dash-deployment-server/private-packages',
            '/dash-deployment-server/configure-system-dependencies',
            '/dash-deployment-server/redis-database',
            '/dash-deployment-server/celery-process',
            '/dash-deployment-server/environment-variables',
            '/dash-deployment-server/map-local-directories',
            '/dash-deployment-server/staging-app',
            '/dash-deployment-server/pdf-service',
            '/dash-deployment-server/troubleshooting',
            '/dash-deployment-server/analytics',
            '/dash-deployment-server/logs',
            '/dash-deployment-server/support',
            '/dash-deployment-server/git'
        ]

        def visit_and_snapshot(href):
            self.driver.get('http://localhost:8050{}'.format(href))
            # stub elem at the bottom of browser
            try:
                self.wait_for_element_by_id('wait-for-page-{}'.format(href))
                if href == '/external-resources':
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.snapshot(href)
                self.driver.back()
            except Exception as e:
                print(href)  # determine which page is having issues
                raise e
        for link in links:
            if link.startswith('/') and link != '/dash-daq' and link != '/dash-bio':
                visit_and_snapshot(link)

        # test search page
        self.driver.get('http://localhost:8050/search')
        self.wait_for_element_by_id('search-input')
        self.snapshot('search-blank')
        search_element = self.driver.find_element_by_id('search-input')
        search_element.clear()
        search_element.send_keys('dropdown')
        self.wait_for_element_by_css_selector('#hits .ais-hits--item')
        self.snapshot('search-dropdown')
