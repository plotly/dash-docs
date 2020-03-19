import dash_core_components as dcc
import dash_html_components as html
import json
from textwrap import dedent

def Collapsible(title, contents=None, description=None):
    return html.Details([
        html.Summary(title),
        html.Div(contents)
    ])


def Sidebar(urls, depth=0):

    chapters = []
    for chapter in urls:
        try:
            if 'chapters' in chapter and not chapter.get('hide_chapters_in_sidebar', False):
                chapters.append(Collapsible(
                    chapter['name'],
                    Sidebar(chapter['chapters'], depth+1),
                    chapter.get('description', None)
                ))
            else:
                title = ''
                if isinstance(chapter.get('description'), str):
                    title = dedent(chapter['description']).strip()
                elif isinstance(chapter.get('description_short'), str):
                    title = dedent(chapter['description_short']).strip()

                chapters.append(html.Div(
                    dcc.Link(
                        chapter['name'],
                        href=chapter['url'].rstrip('/'),
                    ),
                    className='link',
                    **(
                        {'title': title}
                        if not title == '' else {}
                    )
                ))
        except Exception as e:
            print(e)

    return html.Div(
        className='sidebar sidebar--{}'.format(depth),
        children=chapters
    )
