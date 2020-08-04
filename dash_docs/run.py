# -*- coding: utf-8 -*-
from copy import deepcopy

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from .server import app, server

from .import chapter_index
from dash_docs import tools
from dash_docs.chapters.home.index import layout as home

import dash_user_guide_components as dugc


def create_contents(contents):
    h = []
    for i in contents:
        if isinstance(i, list):
            h.append(create_contents(i))
        else:
            h.append(html.Li(i))
    return html.Ul(h)


SIDEBAR_INDEX = deepcopy(chapter_index.URLS)
chapter_index.index_pages(SIDEBAR_INDEX)
chapter_index.create_urls_without_content(SIDEBAR_INDEX)

header = html.Div(
    className='header',
    children=html.Div(
        className='container-width',
        style={'height': '100%'},
        children=[

            html.Span([
                html.A(html.Img(
                    src='/assets/images/logo-plotly.png',
                ), href='https://plotly.com'),
                html.Img(
                    src='/assets/images/logo-seperator.png',
                ),
                dcc.Link(html.Img(
                    src='/assets/images/logo-dash.png',
                ), href='/', id='logo-home'),
            ], className='logo'),

            # HEADS UP!
            # If you are modifying these header links,
            # make sure to check that the responsive design still works
            # The breakpoints are set in override.css
            html.Div(className='links', children=[
                html.A('Announcements', href='https://community.plotly.com/tag/announcements'),
                html.A('Gallery', href='https://dash-gallery.plotly.host'),
                html.A('Show & Tell', href='https://community.plotly.com/tag/show-and-tell'),
                html.A('Community Forum', href='https://community.plotly.com/c/dash'),
                html.Iframe(
                    src="https://ghbtns.com/github-btn.html?user=plotly&repo=dash&type=star&count=true&size=small",
                    style={
                        'border': 'none',
                        'height': '30px',
                        'verticalAlign': 'middle',
                        'marginTop': '9px',
                        'width': '120px'
                    }
                ),
            ])
        ]
    )
)

DEFAULT_AD = dict(
    alt='Ad for Dash Enterprise: A Kubernetes platform for rapid Dash app deployment.',
    src=tools.relpath('/assets/images/sidebar/dash-enterprise-kubernetes.jpg'),
    href='https://plotly.com/dash/kubernetes/?utm_source=docs&utm_medium=sidebar&utm_campaign=june&utm_content=kubernetes'
)

app.title = 'Dash User Guide and Documentation - Dash by Plotly'

app.layout = html.Div(
    [
        # div used in tests
        html.Div(id='wait-for-layout'),

        dcc.Location(id='location', refresh=False),

        header,

        html.Div(className='content-wrapper', children=[
            html.Div([
                dugc.Sidebar(urls=SIDEBAR_INDEX),
                html.A([
                    html.Img(
                        id='sidebar-image-img',
                        className='sidebar-image',
                        src=DEFAULT_AD['src'],
                        alt=DEFAULT_AD['alt']
                    ),
                    html.Div(id='fade-out')
                ], id='sidebar-image-link', href=DEFAULT_AD['href']),
            ], className='sidebar-container'),

            html.Div([
                html.Div(id='backlinks-top', className='backlinks'),
                html.Div(
                    html.Div(id='chapter', className='content'),
                    className='content-container'
                ),
                html.Div(id='backlinks-bottom', className='backlinks'),
            ], className='rhs-content container-width'),

            dugc.PageMenu(id='pagemenu')

        ]),

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
        dcc.Link('Home', href='/')
    ]
    for i, part in enumerate(parts[:-1]):
        href='/' + '/'.join(parts[:i + 1])
        name = chapter_index.URL_TO_BREADCRUMB_MAP.get(href, '? {} ?'.format(href))
        links += [
            html.Span(' > '),
            dcc.Link(name, href=href)
        ]
    current_chapter_name = chapter_index.URL_TO_BREADCRUMB_MAP.get(
        pathname.rstrip('/'), '? {} ?'.format(pathname)
    )
    links += [html.Span(' > ' + current_chapter_name)]
    return links


def flat_list(*args):
    out = []
    for arg in args:
        out += arg if isinstance(arg, list) else [arg]

    return out

@app.callback([Output('chapter', 'children'),
               Output('backlinks-top', 'children'),
               Output('backlinks-top', 'style'),
               Output('backlinks-bottom', 'children'),
               # dummy variable so that a loading state is triggered
               Output('pagemenu', 'dummy2'),
               Output('sidebar-image-img', 'src'),
               Output('sidebar-image-link', 'href')],
              [Input('location', 'pathname')])
def display_content(pathname):
    if pathname is None or pathname == '/':
        return [home, '', {'borderBottom': 'none'}, '', '', DEFAULT_AD['src'], DEFAULT_AD['href']]
    pathname = pathname.rstrip('/')

    backlinks = create_backlinks(pathname)
    def make_page(page_path):
        return flat_list(
            chapter_index.URL_TO_CONTENT_MAP[page_path],
            html.Div(id='wait-for-page-{}'.format(page_path)),
        )

    if pathname in chapter_index.URL_TO_CONTENT_MAP:
        children = make_page(pathname)

    elif pathname == '/all':
        children = build_all()

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

        children = flat_list(warning_box, home)

    # update the sidebar ad
    ad = DEFAULT_AD['src']
    adhref = DEFAULT_AD['href']
    if (pathname in chapter_index.URL_TO_META_MAP and
            'ad' in chapter_index.URL_TO_META_MAP[pathname]):
        ad = tools.relpath('/assets/images/sidebar/{}'.format(
            chapter_index.URL_TO_META_MAP[pathname]['ad']
        ))
        adhref = chapter_index.URL_TO_META_MAP[pathname]['adhref']
    return [
        children,
        backlinks,
        {'borderBottom': 'thin lightgrey solid'},
        backlinks,
        '',
        ad,
        adhref
    ]


# dummy callback to trigger a pagemenu rerender
app.clientside_callback(
    '''
    function(children) {
        return '';
    }
    ''',
    Output('pagemenu', 'dummy'),
    [Input('chapter', 'children')],
)


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8060)
