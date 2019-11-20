import dash_html_components as html
import json

from .Chapter import Chapter
from .Section import Section


def TOCChapters(chapters):
    chapter_content = []
    for chapter in chapters:
        try:
            if 'url' not in chapter:
                chapter_content.append(Chapter(
                    chapter['name'],
                    chapter['chapters'][0]['url'].rstrip('/'),
                    chapter['chapters'][0]['description']
                ))

            else:
                chapter_content.append(Chapter(
                    chapter['name'],
                    chapter['url'].rstrip('/'),
                    chapter.get('description', '')
                ))
        except Exception as e:
            print(e)

    return chapter_content


def TOC(urls):
    sections = []
    for section in urls:
        sections.append(Section(
            title=section['name'],
            links=TOCChapters(section['chapters']),
            description=section.get('description', None)
        ))
    return html.Div(sections, className='toc')
