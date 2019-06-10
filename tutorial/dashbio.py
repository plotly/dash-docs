import dash_core_components as dcc
import dash_html_components as html
from tutorial import styles
from tutorial.utils.dashbio_docs import generate_docs

import dash_bio

dashbio_library_heading = [
    dcc.Markdown('''# Dash Bio'''),

    dcc.SyntaxHighlighter('''pip install dash-bio=={}'''.format(dash_bio.__version__),
                          customStyle=styles.code_container),

    dcc.Markdown('''
    Dash is a web application framework that provides pure Python abstraction
    around HTML, CSS, and JavaScript.

    Dash Bio is a suite of bioinformatics components that make it simpler to
    analyze and visualize bioinformatics data and interact with them in a Dash
    application.

    The source can be found on GitHub at [plotly/dash-bio](https://github.com/plotly/dash-bio).

    These docs are using Dash Bio version {}.
    '''.replace('    ', '').format(dash_bio.__version__, dash_bio.__version__)
    )
]

dashbio_install_instructions = dcc.SyntaxHighlighter('''>>> import dash_bio
    >>> print(dash_bio.__version__)
    {}'''.replace('    ', '').format(dash_bio.__version__),
    customStyle=styles.code_container)


dashbio_components = {

    'AlignmentChart': {
        'description': '''An alignment chart.''',
        'datafile': {
            'name': 'alignment_viewer_p53.fasta',
            'parameter': 'data'
        },
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/alignment_chart',
            'height': 950
        }
    },

    'Circos': {
        'description': '''A circular ideogram with arcs representing links between genes.''',
        'library_imports': [
            ['json', 'json'],
        ],
        'datafile': {
            'name': 'circos_graph_data.json'
        },
        'params': {
            'layout': 'circos_graph_data[\'GRCh37\']',
            'tracks': '''[{
  'type': 'CHORDS',
  'data': circos_graph_data['chords'],
  'opacity': 0.7,
  'color': {'name': 'color'},
  'config': {
    'tooltipContent': {
      'source': 'source',
      'sourceID': 'id',
      'target': 'target',
      'targetID': 'id',
      'targetEnd': 'end'
    }
  }
}]'''
        },
        'setup_code': '''circos_graph_data = json.loads(data)''',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/circos',
            'height': 700
        }
    },

    'Clustergram': {
        'description': '''A heatmap with dendrograms to display clustering of
        data such as gene expression data.''',
        'default_id': False,
        'library_imports': [
            ['pandas', 'pd'],
            ['dash_core_components', 'dcc']
        ],
        'params': {
            'data': 'data',
            'color_threshold': '{\'row\': 150, \'col\': 700}',
            'column_labels': 'list(df.columns.values)',
            'row_labels': 'list(df.index)',
            'hide_labels': '[\'row\']',
            'height': '800',
            'width': '600'
        },
        'component_wrap': 'dcc.Graph(figure=_[0])',
        'setup_code': '''df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/clustergram_mtcars.tsv',
        sep='\t', skiprows=4).set_index('model')
data = df.values''',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/clustergram',
            'height': 850
        }
    },

    'Ideogram': {
        'description': '''A visual representation and analysis tool for chromosome bands.''',
        'params': {
            'chrHeight': '250'
        },
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/ideogram'
        }
    },
    'ManhattanPlot': {
        'description': '''A plot that can be used to display the results of genomic studies
        sorted out by chromosome. Perfect for Genome Wide Association Studies (GWAS).''',
        'default_id': False,
        'component_wrap': 'dcc.Graph(figure=_)',
        'params': {
            'dataframe': 'df'
        },
        'library_imports': [
            ['pandas', 'pd'],
            ['dash_core_components', 'dcc']
        ],
        'setup_code': '''df = pd.read_csv("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/manhattan_data.csv")''',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/manhattan',
            'width': 800
        }
    },
    'Molecule3dViewer': {
        'description': '''A 3D visualization of biomolecular structures.''',
        'params': {
            'modelData': 'model_data',
            'styles': 'styles_data',
            'backgroundOpacity': '\'0\''
        },
        'library_imports': [
            ['json', 'json'],
            ['urllib.request', 'urlreq']
        ],
        'setup_code': '''model_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/model_data.js').read()
styles_data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/mol3d/styles_data.js').read()
model_data = json.loads(model_data)
styles_data = json.loads(styles_data)
''',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/mol3d'
        }
    },
    'NeedlePlot': {
        'description': '''A combination of a bar chart and a scatter plot, for data that are
        both categorical and continuous.''',
        'library_imports': [
            ['json', 'json']
        ],
        'params': {
            'mutationData': 'mdata'
        },
        'datafile': {
            'name': 'needle_PIK3CA.json'
        },
        'setup_code': '''mdata = json.loads(data)''',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/needle_plot',
            'width': 850
        }
    },

    'OncoPrint': {
        'description': '''A chart that can be used to visualize multiple
        genomic alternations with an interactive heatmap.''',
        'library_imports': [
            ['json', 'json']
        ],
        'datafile': {
            'name': 'oncoprint_dataset3.json',
            'parameter': 'data'
        },
        'setup_code': '''data = json.loads(data)
''',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/oncoprint',
            'width': 900
        }
    },

    'SequenceViewer': {
        'description': '''A sequence viewer.''',
        'params': {
            'sequence': '\"MALWMRLLPLLALLALWGPDPAAAFVN\
QHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLA\
LEGSLQKRGIVEQCCTSICSLYQLENYCN\"'
        }
    },

    'Speck': {
        'description': '''A 3D WebGL molecule viewer.''',
        'params': {
            'view': '{\'resolution\': 600}'
        },
        'datafile': {
            'name': 'speck_methane.xyz',
            'parameter': 'data'
        },
        'library_imports': [
            ['dash_bio.utils.xyz_reader', 'xyz_reader']
        ],
        'setup_code': '''data = xyz_reader.read_xyz(data_string=data)''',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/speck',
            'height': 500
        }
    },

    'VolcanoPlot': {
        'description': '''A graph that can be used to identify clinically meaningful markers in
        genomic experiments.''',
        'default_id': False,
        'library_imports': [
            ['pandas', 'pd'],
            ['dash_core_components', 'dcc']
        ],
        'setup_code': '''df = pd.read_csv("https://raw.githubusercontent.com/plotly/dash-bio/master/tests/dashbio_demos/sample_data/volcano_data1.csv")''',
        'params': {
            'dataframe': 'df'
        },
        'component_wrap': 'dcc.Graph(figure=_)',
        'iframe_info': {
            'location': 'https://dash-bio.plotly.host/docs-demos-dashbio/volcano',
            'width': 800
        }
    }
}

layout_children = generate_docs(
    'dash_bio',
    'dashbio',
    dashbio_library_heading,
    dashbio_install_instructions,
    dashbio_components
)

layout = html.Div(className="gallery", children=layout_children)
