## Dash callback triggered when drawing annotations

When using a plotly figure in a `dcc.Graph` component in a Dash app, drawing a shape on the figure will modify the `relayoutData` property of the `dcc.Graph`. You can therefore define a callback listening to `relayoutData`. In the example below we display the content of `relayoutData` inside an `html.Pre`, so that we can inspect the structure of `relayoutData` (when developing your app, you can also just print the variable inside the callback to inspect it).

