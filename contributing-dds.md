# Dash Deployment Server Documentation

The Dash Deployment Server documentation `/dash-deployment-server/` consists of a series of chapters relevant to Plotly Enterprise + DDS users. If you wish to contribute to these documents, please follow the instruction below.

## Editing Existing Content

If you would like to edit or add content to an existing chapter (e.g. "Linking to Redis Database"), then navigate `tutorial/dash_deployment_server_examples.py` and edit the content within the layout variable (e.g. `Redis`).

## Contributing New Chapter

### Relevant Files

Files that need edited include:
- `tutorial/dash_deployment_server_examples.py` Home to chapter content.
- `tutorial/dash_deployment_server.py` Defines the layout of `dash.plot.ly/dash-deployment-server/`
- `tutorial/chapter_index.py` Defines the layout of `dash.plot.ly` and the search index.
- `tests/test_intergration.py` Links for Percy snapshots.

### Add New Chapter

In `tutorial/dash_deployment_server.py` add the new chapter to the Dash Deployment Server main page.

```
reusable_components.Chapter(title, URL, description)
```

For example,

```
reusable_components.Chapter('Linking a Redis Database',
            '/dash-deployment-server/redis-database',
            'Create and link an in-memory database to your Dash Apps.')
```

### Add Chapter Content

In `tutorial/dash_deployment_server_examples.py` create a variable to define the chapter layout content.

```
NewChapter = html.Div(children=[
    html.H1('Chapter Heading'),
    dcc.Markdown(s('''

    ### Title

    text
    '''))
])
```

##### Best Practices

When adding **text** use: ```dcc.Markdown(s())```    
When adding **code** use: ```dcc.Markdown(s())``` with triple backticks.
When adding **images** add the images to `tutorial/assets/images/dds/` and use a relative link in the text.      
When adding **links** use relative links where possible.

### Update Chapter Index

In `tutorial/chapter_index.py` add a new dict entry for your chapter.

```
'NewChapter-examples': {
      'url': '',
      'content': '',
      'name': '',
      'description': ''
  },
```

For example,

```
'redis-examples': {
      'url': '/dash-deployment-server/redis-database',
      'content': dds_examples.Redis,
      'name': 'Linking a Redis Database',
      'description': 'Create and link an in-memory database to your Dash Apps.'
  },
```

Next, because you have edited the chapters dict, which is used to generate the search index, you need to update the search index by running `python dash_search_index.py` in the _root_ of the dash-docs repo.

### Add Links to Test

Lastly, in `tests/test_intergration.py` you'll need to add the new URL link to the existing DDS list, which will enable Percy to capture snapshots of the new chapter.
