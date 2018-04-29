# Update dash-doc search index: https://www.algolia.com/apps/7EK9KHJW8M/explorer/browse/dash_docs

import os

from algoliasearch import algoliasearch
from tutorial.chapter_index import chapters

# Algolia Credentials
client = algoliasearch.Client('7EK9KHJW8M', os.environ['ALGOLIA_API_KEY'])
index = client.init_index('dash_docs')

dash_index = []

for chapter in chapters:
    chap = {}
    chap['name'] = chapters[chapter]['name']
    chap['permalink'] = 'https://plot.ly'+chapters[chapter]['url']
    chap['description'] = chapters[chapter]['description']
    if chapter not in ['getting-started', 'getting-started-part-2', 'graphing']:
        chap_content = str(chapters[chapter]['content'])
        chap_content = chap_content.replace("'", '')
        chap_content = chap_content.replace('"', '')
        chap_content = chap_content.replace('\\n', '')
        chap['content'] = chap_content
    else:
        chap['content'] = ''
    dash_index.append(chap)

# clear existing remote index and push dash_index to algolia
index.clear_index()
index.add_objects(dash_index)
