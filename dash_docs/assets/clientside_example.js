window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        update_graph: function(data, scale) {
        return {
            'data': data,
            'layout': {
                 'yaxis': {'type': scale}
             }
        };
    }
    }
});