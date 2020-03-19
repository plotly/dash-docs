#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from dash_docs import chapter_index
import plotly


def generate_sidebar_index():
    # It is safe to mutate URLS since we're only using this variable in a script
    # Otherwise, we'd want to make a copy of it
    chapter_index.index_pages(chapter_index.URLS)
    chapter_index.create_urls_without_content(chapter_index.URLS)
    return json.dumps(chapter_index.URLS, indent=2, cls=plotly.utils.PlotlyJSONEncoder)

if __name__ == '__main__':
    with open('SIDEBAR-INDEX.json', 'w') as f:
        f.write(generate_sidebar_index())
