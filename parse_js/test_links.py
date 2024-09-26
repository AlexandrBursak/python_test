#
# Copyright 2021 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc. Confidential.
#
# This is unpublished proprietary source code of DataRobot, Inc.
# and its affiliates.
#
# The copyright notice above does not evidence any actual or intended
# publication of such source code.
from __future__ import absolute_import, print_function

import os
import os.path
import re
from itertools import product

# import pytest
# import requests
from future.moves.urllib.parse import urljoin

# from predictions_monitor.integrations.context_builder import WebServerContextBuilder

# FIXTURES #########################################################################################

current_dir = os.path.dirname(os.path.realpath(__file__))
tests_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
datarobot_dir = os.path.abspath(os.path.join(tests_dir, os.pardir))

# although unlikely, this allows for custom links per language if necessary.
EN_PREDICTION_DOCS_PATH = 'predictions/api/dr-predapi.html'
JP_PREDICTION_DOCS_PATH = 'predictions/api/new-prediction-api.html'
PT_PREDICTION_DOCS_PATH = 'predictions/api/new-prediction-api.html'

app_host = os.getenv('APP_HOST', 'http://localhost/')
docs_prefixes = (
    '/docs/',
    '/docs-jp/',
    # '/docs-pt/'
)
docs_path_prefixes = [urljoin(app_host, prefix) for prefix in docs_prefixes]
print('--> PEAK docs_path_prefixes:', docs_path_prefixes)
docs_links_file = os.path.abspath(os.path.join(current_dir, 'doc-links.js'))
print('--> PEAK docs_links_file:', docs_links_file)
snippet_paths = (
    EN_PREDICTION_DOCS_PATH,
    JP_PREDICTION_DOCS_PATH,
    PT_PREDICTION_DOCS_PATH,
)
snippet_links = [urljoin(prefix, path) for prefix, path in zip(docs_path_prefixes, snippet_paths)]
full_test_list = []
admin_user_credentials = dict(username='docs-user@datarobot.com', password='testing123')

def modify_part_of_parse_code(item):
    item = re.sub(r"\[DOCBOOKS\.HTML\]", '"html"', item, 0, re.DOTALL | re.IGNORECASE | re.MULTILINE)
    item = re.sub(r"\[DOCBOOKS\.ENT_HTML\]", '"ent_html"', item, 0, re.DOTALL | re.IGNORECASE | re.MULTILINE)
    return item

def extract_inapp_doc_links():
    """ Gets the list of in-app links in the UI that link to the User Docs """
    regex = r'return\s(getLinkForCurrentDocBook\([^;]+\)(?:[^;]*))'
    with open(docs_links_file) as f:
        paths = (modify_part_of_parse_code(path) for path in re.findall(regex, f.read()) if '.html' in path)
    return set(paths)


def append_to_list_URL(item, link):
    full_test_list.append(os.path.join(item, link.split('#')[0]))


def getLinkForCurrentDocBook(defaultLink = None, mkdocsLink = None):
    # if isinstance(defaultLink, str):
    #     full_test_list.append(os.path.join(docs_path_prefixes[2], defaultLink.split('#')[0]))
    # else:
    #     full_test_list.append(os.path.join(docs_path_prefixes[2], defaultLink.get('html').split('#')[0]))

    if mkdocsLink is not None:
        if isinstance(mkdocsLink, str):
            [append_to_list_URL(item, mkdocsLink.split('#')[0]) for item in docs_path_prefixes]
        else:
            [append_to_list_URL(item, mkdocsLink.get('html').split('#')[0]) for item in docs_path_prefixes]


def generate_list_of_urls():
    for link in extract_inapp_doc_links():
        link = re.sub(r"\n", '', link, 0, re.MULTILINE)
        exec(link)

generate_list_of_urls()
print('full_test_list:', len (full_test_list), full_test_list)

# TESTS ############################################################################################
# @pytest.fixture()
# def logged_in_browser_session():
#     session = requests.session()
#     resp = session.post(urljoin(app_host, '/account/login'), json=admin_user_credentials).json()
#     assert 'uid' in resp
#     return session


# @pytest.mark.parametrize('link', extract_inapp_doc_links())
# def test_inapp_doc_link_exists(link, logged_in_browser_session):
#     resp = logged_in_browser_session.get(link)
#     assert resp.status_code == 200

