# Update dash-doc search index: https://www.algolia.com/apps/7EK9KHJW8M/explorer/browse/dash_docs

import os
import sys

from algoliasearch import algoliasearch
from tutorial.chapter_index import chapters

# Algolia Credentials
client = algoliasearch.Client('7EK9KHJW8M', os.environ['ALGOLIA_API_KEY'])
index = client.init_index('dash_docs')

dash_index = []

for chapter in chapters:
    chap = {}
    chap['name'] = chapters[chapter]['name']
    chap['permalink'] = 'https://dash.plotly.com'+chapters[chapter]['url']
    chap['description'] = chapters[chapter]['description']
    chap_content = str(chapters[chapter]['content'])
    chap_content = chap_content.replace("'", '')
    chap_content = chap_content.replace('"', '')
    chap_content = chap_content.replace('\\n', '')
    # Algolia limits records to ~20000 bytes
    # This will check content size & reduce chap_content for those pages
    # that surpass the limit.
    # Note the chap_content section is just used to beef up search options,
    # it is not user-facing like the above attributes
    if sys.getsizeof(chap_content) < 19000:
        chap['content'] = chap_content
    else:
        chap['content'] = chap_content[0:10000]
    dash_index.append(chap)

# clear existing remote index and push dash_index to algolia
index.clear_index()
index.add_objects(dash_index)
