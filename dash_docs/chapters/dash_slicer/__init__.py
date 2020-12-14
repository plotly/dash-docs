import sys
import dash_html_components as html


if sys.version_info > (3, ):
    from .import index
else:

    class FakeModule:
        pass

    index = FakeModule()
    index.layout = html.Div("Dash Slicer is not supported on Python 2.7")
