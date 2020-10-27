import dash_html_components as html
import dash_core_components as dcc
from dash_docs import reusable_components as rc
import os
import jupytext
from dash_docs import tools
from dash_docs import styles


def load_notebook(path, relative_path=False):
    if relative_path:
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    notebook = jupytext.read(path)
    notebook_cells = notebook["cells"]
    layout_elements = []
    for cell in notebook_cells:
        if cell["cell_type"] == "markdown":
            layout_elements.append(rc.Markdown(cell["source"]))
        elif cell["cell_type"] == "code":
            code_text, code_block = tools.load_block(cell["source"], nb_cell=True)
            layout_elements.append(rc.Markdown(code_text, style=styles.code_container))
            layout_elements.append(html.Div(code_block, className="example-container"))
    return layout_elements


path = "./dash-annotations.md"
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


layout = html.Div(load_notebook("./dash-annotations.md", relative_path=True))
