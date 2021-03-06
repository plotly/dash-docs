import dash_html_components as html
from .import Markdown
from textwrap import dedent
from .Markdown import Markdown
import copy

def CreateDisplay(scope):
    def Display(example_string):
        scope_copy = copy.copy(scope)
        if 'result = ' in example_string:
            try:
                exec(dedent(example_string), scope_copy)
            except Exception as e:
                print('\n\nError running this example:\n')
                print(dedent(example_string))
                raise e
            result = scope_copy['result']
            example_string = example_string.replace('result = ', 'app.layout = ')
        else:
            try:
                result = eval(dedent(example_string), scope)
            except Exception as e:
                print('\n\nError running this example:\n')
                print(dedent(example_string))
                raise e
        if '# no-display' in example_string:
            example_string='\n'.join([
                s for s in example_string.split('\n')
                if '# no-display' not in s
            ])
        return html.Div([
            Markdown(
                '```python  \n' + dedent(example_string).strip() + '\n```',
                style={'marginBottom': 10, 'borderLeft': 'thin #C8D4E3 solid'}
            ),
            result
        ])
    return Display
