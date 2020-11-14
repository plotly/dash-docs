import os
import dash_html_components as html
import dash_core_components as dcc
from dash_docs import reusable_components as rc
from dash_docs import tools
from dash_docs import styles

dirname = os.path.dirname(os.path.relpath(__file__))
examples_dir = os.path.join(dirname, 'examples')
examples_list = ['annotations101', 'annotations_callback', 'drawing_tools', 'annotation_style', 'region_extraction',
        'path_extraction', 'modify_shapes', 'modify_shapes_part2']

examples = tools.load_examples(__file__)

layout_elements = []
for example in examples_list:
    with open(os.path.join(examples_dir, example + '.md')) as f:
        layout_elements.append(
            rc.Markdown(
                f.read()
                ))
    layout_elements.append(
        rc.Markdown(
          examples[example + ".py"][0],
          style=styles.code_container
        ))
    layout_elements.append(
        html.Div(examples[example + ".py"][1], className='example-container'),
            )


layout = html.Div(layout_elements)
