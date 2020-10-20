# Performance

## Performance Strategies
1. Speed up your callbacks

    The faster your callbacks execute, the more requests
    your backend will be able to process and the faster
    your users will see updates.

    See [/callback-speed] for more.

2. Prepare data in advance with a periodic background jobs

    If you need to display recent data and fetching the data
    from the underlying source (e.g. a database, an API or S3)
    is slow, expensive, or unable to handle the load, then
    consider fetching your data in a background
    queue with Celery and storing the results in Redis or Postgres.
    Your callbacks or `layout` function will load the data from
    Redis or Postgres instead of fetching it on-the-fly.

    See [Sample X], [Sample Y] for details.

3. Scale up your backend

    

4. Write clientside callbacks
5. Reduce volume & frequency of data on wire
6. Use high performance rendering methods
7. Loading states
8. `plotly.js` bundle

## Measuring Performance
1. Callback graph
2.

## Deep Dive


## You Click on a Button - What Happens?

To understand Dash performance, one must understand the data flow
in Dash apps.

1. Data in backend

    Dash app starts when `gunicorn` etc

    We encounter this during hot-reload development but
    it doesn't affect your end users as long as you've
    set up zero-downtime deploys.

    For development:
        - Consider Jupyter.
        - Consider arrow.

2. Index page is served

    - Nothing to do here, but there are some hooks available

3. JavaScript bundles are served

    - `serve_locally=False`
    - `plotly.js` bundle

4. Data served up by `/_dash-layout`

    Network request number 1.

    Things to consider: `serve_layout`

5. User Interaction

    Sometimes user interactions don't involve network requests.
    For example:
    - Hovering over a graph if you aren't subscribed to
    `hoverData`
    - In `dcc.Input`, listening to `n_blur` instead of `value`

6. Callback Request Part 1: Request made over network from client's browser to your backend

7. [...] Part 2: Backend deserializes request

    You don't have any control over this.
    As a framework, we might consider faster serialization in the future.

8. [...] Part 3: Backend calls your callback

9. [...] Part 4: Backend serializes your response

10. [...] Part 5: Backend sends response back to client

11. [...] Part 6: Dash's front end processes request (bookkeeping)

    You don't have any control over this.
    We recently optimized these pathways.

12. [...] Part 7: Dash's component rerenders with the new data

## Finding the Bottleneck

1. Speed of Request
2. Throughput
    - Celery
3. Data Volume

- Dev Tools
- Timing Python Functions - Jupyter %timeit?
- Measure in Production
    - Local will be very different than remote
- Create a reproducible example to prove your hypothesis

## Performance Strategies

1. Measure, measure, measure

2. Consider the Data Flow

- Caching data in the backend
- Running background jobs

3. Improve the Speed of your Computations

- Add a decorator
    - `@numba`
    - `redis.cache`

- Numpy instead of Python lists
- Vaex
- RAPIDs
- Dask
- If you're a DE customer, see our sample apps ...

4. Improve File System IO

Use Arrow
Use SSD

5. Use a Faster Data Store

- Load things into memory
- Or don't load things into memory - perform computations on database
- Cache things?

SQL
- Precomputed queries
- Index things
- Query optimizer?
- Use `ibis` because it might optimize for you?

Column Stores
- Vaex

6. Clientside callbacks
    - Simple ops like changing the color. See the example in clientside callbacks section.
    - Transcrypt

7. Scaling Workers or Containers

Job Queues
Web Processes

Pitch DE on K8S

8. Reduce Data on the Wire - Clientside vs Serverside Ops
    - Datashader
    - DataTable
    - Histogram
    - Box Plot
    - Sharing Data Between Callbacks Server Side instead of `dcc.Store`
    - `dcc.Tabs`

9. Reduce the Amount of Stuff Rendered in the Browser

    - `DataTable` virtualization vs `html.Table`
    - Same visualization with less data?
    - Similar to Reduce Data on the Wire

10. Reduce Number of Requests
    - `value` vs `n_blur`
    - `prevent_initial_call=True`
    - Slider drag mode
    - Combining Callbacks with Multiple Outputs or Pattern-Matching Callbacks

11. Use Component's Faster Pathway
    - `dcc.Graph` - `scattergl`
    - `DataTable` `virtualized` vs `html.Table` or not
    - Use a different component library. For example, `dash_leaflet`

    But no matter how fast the component renders,
    you're still sending data over the wire.

12. Load Data into Memory (Local Cache)

    If you can afford it

13. Use Faster Hardware

    Is there a Dash Enterprise angle here?

    SSD with Vaex

    Move away from Heroku

14. Use Faster Network

    Move server closer to end user

    Move databases closer to Dash apps

    Network throughput on GCP?

15. Make plotly.js bundle smaller

## Edge Cases

**Tens of thousands of callbacks**

- `/_dash-dependencies` could become large
- Dash's front-end might not be optimized for this
- Consider wildcard callbacks

**Tens of thousands of components**

- `html.Table` vs `DataTable`

## Perceived Performance

1. Minimizing User Interaction

Saving their selections:
    - Persistence
    - Snapshot Engine

2. Loading States

- Reduce flicker
- Tell users how long it will take
- Link to 99PI podcast

3. Persistence plus dcc.Store? Is there a recipe here?

## Road Ahead

- Sponsor these improvements
- Composite components that do things for you like:
    - `DataShader`
    - `DataTable`
- Better Loading Components
- More webgl
- Clientside caching
- List out things that were sponsored
