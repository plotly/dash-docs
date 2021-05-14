## app&#46;py

By convention, this is usually called `app.py` or `index.py`. This file is 
called by the command you specify in your `Procfile`. It will contain your Python
code and must be placed in your project's root directory. This file must also contain a 
line that defines the `server` variable so that it can be exposed for the 
`Procfile`:

```python
import dash

app = dash.Dash(__name__)
server = app.server
...

```

---
