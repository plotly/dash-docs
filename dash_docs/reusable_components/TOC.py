import dash_html_components as html

from .Chapter import Chapter
from .Section import Section


def TOCChapters(chapters):
    chapter_content = []
    for chapter in chapters:
        try:
            if 'url' not in chapter:
                chapter_content.append(Chapter(
                    chapter['name'],
                    href=chapter['chapters'][0]['url'].rstrip('/'),
                    caption=chapter['chapters'][0].get('description', ''),
                    className=chapter['chapters'][0].get('className', ''),
                    icon=chapter['chapters'][0].get('icon', ''),
                ))

            else:
                chapter_content.append(Chapter(
                    chapter['name'],
                    href=chapter['url'].rstrip('/'),
                    caption=chapter.get('description', ''),
                    className=chapter.get('className', ''),
                    icon=chapter.get('icon', ''),
                ))
        except Exception as e:
            print('Error generating TOC', e)

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
