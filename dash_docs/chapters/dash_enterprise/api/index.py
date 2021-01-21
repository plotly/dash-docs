# -*- coding: future_fstrings -*-

from dash_docs import reusable_components as rc
import dash_html_components as html
from dash_docs import tools
import os

base_url = os.environ.get('BASE_URL', 'https://<your-dash-enterprise-server>')
url, domain = tools.get_url_and_domain(base_url)

query_video = html.Video(style={'width': '100%'}, controls=True, autoPlay=True, children=[
     html.Source(
         src=tools.relpath('/assets/images/gql-api/query.mp4'),
         type='video/mp4',
     ),
])

api_reference_video = html.Video(style={'width': '100%'}, controls=True, autoPlay=True, children=[
     html.Source(
         src=tools.relpath('/assets/images/gql-api/api-reference.mp4'),
         type='video/mp4',
     ),
])

mutation_video = html.Video(style={'width': '100%'}, controls=True, autoPlay=True, children=[
     html.Source(
         src=tools.relpath('/assets/images/gql-api/mutation.mp4'),
         type='video/mp4',
     ),
])

text1 = rc.Markdown(
    children=f"""
# Dash Enterprise App Manager API

The Dash Enterprise App Manager's APIs provide access to the Dash Enterprise backend. Every action that you might perform when interacting with the App Manager UI is performed through the API.

The APIs that the App Manager uses are open and accessible to all Dash Enterprise users. Use these APIs to interact with the platform programmatically. For example, you can use the APIs to build CI/CD pipelines or report platform usage.

The Dash App Manager has two distinct APIs:

* A REST User Management API to interact with the Admin's User Management Panel. This is available at `https://<your-dash-enterprise-server>/Auth/admin/user`. This is used to manage user accounts. This API is available for use but not yet documented. Inspect the network requests in the User Management Panel at {url}/Auth/admin/user to inspect the API requests. Authenticate to this API with your API key (see below).

* A GraphQL API that's used for all the remaining operations that aren't specific to User Management, e.g. managing Dash Applications, Databases, Workspaces, Portal, SSH keys, and more. This API is documented in this chapter.

## Authentication

**API Key**

You will need an API Key for the Dash Enterprise account that will be making the API calls. To acquire an API key for an account, first login to the Dash Enterprise platform and click your username in the top right of the header bar and select "Manage API Key" from the dropdown.

![Manage API Key menu](/assets/images/gql-api/admin-api-key.png)

**Access Privileges**

The API follows the known access privileges. For example if you are using an Admin account API key you will have the ability to access any application irrespective of the application owner. If you are using a non-admin account API key then you'll be restricted to the apps that this account owns.

## GraphQL Background

A [GraphQL](https://graphql.org/learn/queries/) operation can either be a read or a write operation. A GraphQL **query** is used to read or fetch values while a **mutation** is used to write or post values.

GraphQL uses its own query language that allows you to specify just the data that you need.

Queries look like big, nested objects.
Note that the query is not JSON (it's its own special syntax) but the response is JSON.

Here are a couple of examples:

**View the first 10 apps**

`Query`

```
query {{
  apps(page:0, allApps:true) {{
    apps {{
      name
      urlOnServer
      thumbnailUrl
      hasWorkspace
    }}
  }}
}}
```

Example `Response`
```javascript
{{
  "data": {{
    "apps": {{
      "apps": [
        {{
          "name": "aa-chris",
          "urlOnServer": "https://<dash-enterprise>/aa-chris",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-chris-pipeline",
          "urlOnServer": "https://<dash-enterprise>/aa-chris-pipeline",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-chris-timeouts-test",
          "urlOnServer": "https://<dash-enterprise>/aa-chris-timeouts-test",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-hamza-test",
          "urlOnServer": "https://<dash-enterprise>/aa-hamza-test",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-sf-template",
          "urlOnServer": "https://<dash-enterprise>/aa-sf-template",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-tngo-checks",
          "urlOnServer": "https://<dash-enterprise>/aa-tngo-checks",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-tngo-clinical-trial",
          "urlOnServer": "https://<dash-enterprise>/aa-tngo-clinical-trial",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-tngo-conda",
          "urlOnServer": "https://<dash-enterprise>/aa-tngo-conda",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-tngo-crm",
          "urlOnServer": "https://<dash-enterprise>/aa-tngo-crm",
          "thumbnailUrl": null,
          "hasWorkspace": true
        }},
        {{
          "name": "aa-tngo-databricks",
          "urlOnServer": "https://<dash-enterprise>/aa-tngo-databricks",
          "thumbnailUrl": null,
          "hasWorkspace": false
        }}
      ]
    }}
  }}
}}
```

**Get all fields for a particular app**

> Note - We recommend that you don't query the fields that you don't need
> rather than querying all of the fields. Certain fields will take
> much longer to retrieve than other fields and so you can speed up
> your queries by shortening them.

`Query`
```javascript
query {{
  apps(name: "weekly-analytics", allApps: false) {{
    apps {{
      name
      owner {{
        username
      }}
      urlOnServer
      thumbnailUrl
      logs {{
        app
        failed
      }}
      collaborators {{
        users
        teams
      }}
      metadata {{
        title
        description
        tags
        permissionLevel
        showInPortal
        sortRank
      }}
      hasWorkspace
      mounts {{
        hostDir
        targetDir
        status
      }}
      processes {{
        type
        number
        status
      }}
      analytics {{
        appname
      }}
      environmentVariables {{
        name
        value
        status
        readonly
      }}
      linkedServices {{
        name
        serviceType
        created
        status
      }}
      status {{
        running
        deploying
        canScale
      }}
      resources {{
        type
        status
      }}
    }}
  }}
}}
```

> Note - This is a complete list of fields as of Dash Enterprise 4.0.1.
> More fields may have been added in subsequent releases.
> View the GraphiQL Playground (see below) to view the full list of fields.

`Example Response`
```javascript
{{
  "data": {{
    "apps": {{
      "apps": [
        {{
          "name": "weekly-analytics",
          "owner": {{
            "username": "chriddyp"
          }},
          "urlOnServer": "https://dash-playground.plotly.host/api",
          "thumbnailUrl": null,
          "logs": {{
            "app": "",
            "failed": ""
          }},
          "collaborators": {{
            "users": [],
            "teams": []
          }},
          "metadata": {{
            "title": null,
            "description": null,
            "tags": null,
            "permissionLevel": "restricted",
            "showInPortal": false,
            "sortRank": null
          }},
          "hasWorkspace": true,
          "mounts": [],
          "processes": [
            {{
              "type": "web",
              "number": 1,
              "status": ""
            }}
          ],
          "analytics": {{
            "appname": "api"
          }},
          "environmentVariables": [],
          "linkedServices": [],
          "status": {{
            "running": false,
            "deploying": false,
            "canScale": true
          }},
          "resources": []
        }}
      ]
    }}
  }}
}}
```

**Get the owner for a particular app**
`Query`
```javascript
query {{
  apps(name: "weekly-analytics", allApps: false) {{
    apps {{
      owner {{
        username
      }}
    }}
  }}
}}
```

`Example Response`
```javascript
{{
  "data": {{
    "apps": {{
      "apps": [
        {{
          "owner": {{
            "username": "chriddyp"
          }}
        }}
      ]
    }}
  }}
}}
```

**View Which Apps Promoted to the Portal**

> Note Portal "name". This is always "default".
> This field is not exposed in the UI nor configurable.

`Query`
```javascript
query {{
	portals(page:0, name:"default") {{
	  portals {{
	    id
      name
      apps {{
        apps {{
          name
          urlOnServer
          thumbnailUrl
          hasWorkspace
        }}
      }}
	  }}
	}}
}}
```

`Example Response`
```
{{
  "data": {{
    "portals": {{
      "portals": [
        {{
          "id": 1,
          "name": "default",
          "apps": {{
            "apps": [
              {{
                "name": "aa-chris",
                "urlOnServer": "https://dash-playground.plotly.host/aa-chris",
                "thumbnailUrl": null,
                "hasWorkspace": true
              }},
              {{
                "name": "api",
                "urlOnServer": "https://dash-playground.plotly.host/api",
                "thumbnailUrl": null,
                "hasWorkspace": true
              }},
              {{
                "name": "deck-explorer",
                "urlOnServer": "https://dash-playground.plotly.host/deck-explorer",
                "thumbnailUrl": null,
                "hasWorkspace": false
              }}
            ]
          }}
        }}
      ]
    }}
  }}
}}
```

## Graphql API Playground

The GraphQL API Playground is a built-in IDE to test and develop queries and mutations. It is shipped on Dash Enterprise and available at [`/Manager/graphql`]({url}/Manager/graphql).

You need to be logged in to Dash Enterprise to view the GraphQL API Playground.

![GraphQL API Playground blank UI](/assets/images/gql-api/blank.png)

The GraphQL API Playground comes with a built-in API reference for easier navigation. This reference contains the list of queries and mutations, with the `ARGUMENTS` and `TYPE` of each query and mutation.

**The TYPE contains the list of fields that are returned in the response by the API.**

Each type can be clicked on to show more information on it. There are standard types, e.g. `String`, `Boolean`, `Int`, and Dash Enterprise specific types. These are lists of fields, e.g. `Apps`, `App`, `Analytics`, `Owner`.
""")

text2 = rc.Markdown(
    children=f"""
This interface also comes with two important functionalities, **autocompletion** and **error highlighting**. In addition to the built-in reference, these should help when testing and writing queries and mutations.

The autocompletion feature does a typeahead search that finds possible keywords as you type your query. It also auto-fills the custom fields for nested objects when `{{}}` is omitted.

![GraphiQL Playground Autofill](/assets/images/gql-api/autofill.gif)

**Query example**: For a given app, fetch the status, owner, CPU and memory usage.

""")

text3 = rc.Markdown(
    children=f"""
```graphql
query {{
  apps(name: \"example\", allApps: false) {{
    apps {{
      name
      status {{
        running
      }}
      owner {{
        username
      }}
      analytics {{
        resources {{
          cpuUsage
          memoryUsage
        }}
      }}
    }}
  }}
}}
```

**Mutation example**: Create a new app named "my-dash-app".
""")

text4 = rc.Markdown(
    children=f"""
```graphql
mutation {{
  addApp(name: "my-dash-app") {{
    error
    app {{
      name
      owner {{
        username
      }}
    }}
  }}
}}
```

## Python

For the Python example, we'll use the query from the sections above: For a given app, fetch the status, owner, CPU and memory usage.

In order to be able to send GraphQL requests to the API in Python, install the [`gql` package](https://pypi.org/project/gql/):

Import the necessary `gql` classes:

```python
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
```

Instantiate `Client` object with the [API url]({url}/Manager/graphql) and your username and API key as the authentication credentials:

```python
transport = RequestsHTTPTransport(
    url="{url}/Manager/graphql",
    auth=("admin", "your-api-key"),
    use_json=True
)
client = Client(transport=transport)
```

Instantiate the `gql` object with the query or mutation and execute it:

```python
query = gql(
\"""
query {{
  apps(name: "example", allApps: false) {{
    apps {{
      name
      status {{
        running
      }}
      owner {{
        username
      }}
      analytics {{
        resources {{
          cpuUsage
          memoryUsage
        }}
      }}
    }}
  }}
}}
\"""
)
result = client.execute(query)
print(result)
```

## CURL

For the cURL example, we'll use the mutation from the sections above: Create a new app named "my-dash-app".

In a shell, using cURL, this mutation request can be made by executing the following command.

```shell
curl https://your-username:your-password@{domain}/Manager/graphql \\
    -H "Accept-Encoding: gzip, deflate, br" \\
    -H "Content-Type: application/json" \\
    -H "Accept: application/json" \\
    -H "Connection: keep-alive" \\
    -u your-username:your-api-key \\
    --data-binary '{{"query":"mutation {{ addApp(name: \"my-dash-app\") {{ error app {{ name owner {{ username }} }} }} }}"}}' \\
    --compressed
```

This should output:

```json
{{"data":{{"addApp":{{"error":null,"app":{{"name":"my-dash-app","owner":{{"username":"admin"}}}}}}}}}}
```

""",
)

layout = [text1, api_reference_video, text2, query_video, text3, mutation_video, text4]
