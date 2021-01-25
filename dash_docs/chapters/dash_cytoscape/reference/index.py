import dash_html_components as html
import dash_cytoscape as cyto
from dash_docs import reusable_components as rc

layout = html.Div(
    [
        html.H1("Cytoscape Reference"),
        rc.ComponentReference("Cytoscape", cyto),
        html.H2("utils.Tree"),
        rc.Markdown(
            """
    A class to facilitate tree manipulation in Cytoscape.

    **param** node_id: The ID of this tree, passed to the node data dict

    **param** children: The children of this tree, also Tree objects

    **param** data: Dictionary passed to this tree's node data dict

    **param** edge_data: Dictionary passed to the data dict of the edge connecting this tree to its
    parent

    #### Tree.is_leaf()

    **return:** If the Tree is a leaf or not.

    #### Tree.add_children(children)

    Add a list of children to the current children of a Tree.

    **param** children: List of Tree objects

    #### Tree.get_edges()

    Get all the edges of the tree in Cytoscape JSON format.

    **return:** List of dictionaries, each specifying an edge.

    #### Tree.get_nodes()

    Get all the nodes of the tree in Cytoscape JSON format.

    **return:** List of dictionaries, each specifying a node.

    #### Tree.get_elements()

    Get all the elements of the tree in Cytoscape JSON format.

    **return:** List of dictionaries, each specifying an element.

    #### Tree.find_by_id(search_id, method='bfs')

    Find a Tree object by its ID.

    **param** search_id: the queried ID

    **param** method: Which traversal method to use. Either "bfs" or "dfs".

    **return:** Tree object if found, None otherwise.

    #### Tree.create_index()

    Generate the index of a Tree, and set it in place. If there was a previous index, it is
    erased. This uses a BFS traversal. Please note that when a child is added to the tree,
    the index is not regenerated. Furthermore, an index assigned to a parent cannot be
    accessed by its children, and vice-versa.

    **return:** Dictionary mapping node_id to Tree object.

    """
        ),
    ]
)
