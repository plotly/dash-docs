import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

from .server import app, server

from .import chapter_index
from dash_docs import tools
from dash_docs.tutorial import home

from dash_docs.tutorial import search

def create_contents(contents):
    h = []
    for i in contents:
        if isinstance(i, list):
            h.append(create_contents(i))
        else:
            h.append(html.Li(i))
    return html.Ul(h)


header = html.Div(
    className='header',
    children=html.Div(
        className='container-width',
        style={'height': '100%'},
        children=[
            html.A(html.Img(
                src='/assets/images/logo.png',
                className='logo'
            ), href='/'),

            html.Div(className='links', children=[
                html.A('dash enterprise', className='link', href='https://plot.ly/dash/'),
                html.A('user guide', className='link active', href=tools.relpath('/')),
                html.A('plotly', className='link', href='https://plot.ly/'),
                html.A(children=[html.I(className="fa fa-search")], className='link', href=tools.relpath('/search'))
            ])
        ]
    )
)

app.title = 'Dash User Guide and Documentation - Dash by Plotly'

app.layout = html.Div(
    [
        # Stores used by examples.
        dcc.Store(id='memory'),
        dcc.Store(id='memory-output'),
        dcc.Store(id='local', storage_type='local'),
        dcc.Store(id='session', storage_type='session'),
        header,
        html.Div([
            html.Div(id='wait-for-layout'),
            html.Div([
                html.Div(
                    html.Div(id='chapter', className='content'),
                    className='content-container'
                ),
            ], className='container-width')
        ], className='background'),
        dcc.Location(id='location', refresh=False),
    ]
)


def name_to_id(name):
    return (name
            .replace(' ', '-')
            .replace("'", '')
            .replace('?', '')
            .lower() + '-section')


def build_all():
    pdf_contents = []
    table_of_contents = []

    for section in chapter_index.URLS:
        section_content = []
        section_toc = []
        section_id = name_to_id(section['name'])
        section_content.append(html.H1(
            section['name'],
            className='pdf-docs-section-name',
            id=section_id
        ))
        for chapter in section['chapters']:
            if 'chapters' in chapter:
                for i, sub_chapter in enumerate(chapter['chapters']):
                    sub_id = name_to_id(sub_chapter['name'])
                    section_content.append(html.Div(
                        sub_chapter['content'],
                        className='pdf-docs-chapter',
                        id=sub_id
                    ))
                    section_toc.append(html.A(
                        sub_chapter['name'] if i else chapter['name'],
                        href='#{}'.format(sub_id),
                        className='sub-chapter' if i else ''
                    ))
            elif chapter['url'].startswith('http'):
                section_toc.append(html.A(
                    chapter['name'],
                    href=chapter['url']
                ))
            else:
                chapter_id = name_to_id(chapter['name'])
                section_content.append(html.Div(
                    chapter['content'],
                    className='pdf-docs-chapter',
                    id=chapter_id
                ))
                section_toc.append(html.A(
                    chapter['name'],
                    href='#{}'.format(chapter_id)
                ))

        if section_content:
            pdf_contents.append(html.Div(
                section_content,
                className='pdf-docs-section',
                id=section_id
            ))
        # add main section to table of contents
        table_of_contents.append(
            html.A(section['name'],
                   href='#{}'.format(section_id),
                   className='toc-section-link')
        )
        # add all subsections
        table_of_contents.append(
            html.Div(section_toc,
                     className='toc-chapter-links')
        )

    # insert table of contents
    return html.Div([
        html.Div("Dash User Guide and Documentation", id='pdf-docs-title'),
        html.Div(
            [html.H1('Table of Contents')] + table_of_contents,
            id='pdf-docs-toc'
        ),
        html.Div(pdf_contents)
    ], id='pdf-docs')


def create_backlinks(pathname):
    parts = pathname.strip('/').split('/')
    links = [
        dcc.Link('Table of Contents', href='/')
    ]
    for i, part in enumerate(parts[:-1]):
        links += [
            html.Span(' > '),
            dcc.Link(
                part.replace('-', ' ').title(),
                href='/' + '/'.join(parts[:i + 1])
            )
        ]
    links += [html.Span(' > ' + parts[-1].replace('-', ' ').title())]
    return links


def flat_list(*args):
    out = []
    for arg in args:
        out += arg if isinstance(arg, list) else [arg]

    return out


@app.callback(Output('chapter', 'children'),
              [Input('location', 'pathname')])
def display_content(pathname):
    if pathname is None or pathname == '/':
        return home.layout
    pathname = pathname.rstrip('/')

    def make_page(page_path):
        backlinks = create_backlinks(page_path)
        return flat_list(
            backlinks,
            html.Br(),
            chapter_index.URL_TO_CONTENT_MAP[page_path],
            html.Hr(),
            backlinks,
            html.Div(id='wait-for-page-{}'.format(page_path)),
        )

    if pathname in chapter_index.URL_TO_CONTENT_MAP:
        return make_page(pathname)

    elif pathname == '/search':
        return flat_list(create_backlinks(pathname), html.Br(), search.layout)

    elif pathname == '/all':
        return build_all()

    else:
        warning_box = html.Div(
            'Page {} not found'.format(pathname),
            className='warning-box'
        )

        # try to match the head of the path, so we can at least get close
        # to where the user was trying to go
        parts = pathname.lstrip('/').split('/')
        for i in reversed(range(len(parts) - 1)):
            partial_path = '/' + '/'.join(parts[:i + 1])
            if partial_path in chapter_index.URL_TO_CONTENT_MAP:
                return flat_list(warning_box, make_page(partial_path))

        return flat_list(warning_box, home.layout)


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8060)
