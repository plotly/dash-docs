# -*- coding: utf-8 -*-
from dash import Dash
from flask import Flask, redirect, escape, request
import os

class CustomDash(Dash):
    def interpolate_index(self, **kwargs):
        # import later to prevent circular imports - yikes
        from .chapter_index import URL_TO_META_MAP
        # Inspect the arguments by printing them

        kwargs.pop('title')

        meta_kwargs = dict(
            title=URL_TO_META_MAP.get(request.path, {}).get('name', 'Dash User Guide'),
            description=URL_TO_META_MAP.get(request.path, {}).get('description', 'Dash User Guide & Documentation'),
            **kwargs
        )

        return ('''<!DOCTYPE html>
        <html>
            <head>
                {metas}
                <title>{title}</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta
                    name="description"
                    content="{description}"
                >
                <title>{title}</title>
                {favicon}
                {css}
        '''.format(**meta_kwargs) + '''
                <!-- Google Tag Manager Tag -->
                <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
                new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
                j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
                'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
                })(window,document,'script','dataLayer','GTM-N6T2RXG');</script>
            </head>
            <body>
                <!-- Google Tag Manager Tag -->
                <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N6T2RXG"
                    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        ''' + '''
                {app_entry}
                <footer>
                    {config}
                    {scripts}
                    {renderer}
                </footer>
            </body>
        </html>'''.format(**meta_kwargs))


app = CustomDash(
    __name__,
    external_stylesheets=[
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
    ]
)
server = app.server

app.config.suppress_callback_exceptions = True


@server.route('/deployment/on-premise')
def redirectDDS():
    return redirect("/dash-enterprise", code=302)

@server.route('/dash-enterprise/enviornment-variables')
def redirectEnvVar():
    return redirect("/dash-enterprise/environment-variables", code=302)


@server.route('/dash-1-0-migration.')
def redirectMigration():
    return redirect("/dash-1-0-migration", code=302)


@server.route('/gallery')
def redirectGallery():
    return redirect("https://dash-gallery.plotly.host/Portal/", code=302)


@server.route('/dash-deployment-server/<path:subpath>')
def redirectToEnterprise(subpath):
    return redirect('/dash-enterprise/{}'.format(escape(subpath)), code=302)
