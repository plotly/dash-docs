import dash_html_components as html
import dash_vtk
from dash_docs import reusable_components as rc


layout = html.Div([
    rc.Markdown(
        '''
        # Representation Components

        ## GeometryRepresentation

        The properties available on the __GeometryRepresentation__ let you tune the way you want to render your geometry.

        In VTK a representation is composed of an [__Actor__](https://kitware.github.io/vtk-js/api/Rendering_Core_Actor.html), a [__Mapper__](https://kitware.github.io/vtk-js/api/Rendering_Core_Mapper.html) and a [__Property__](https://kitware.github.io/vtk-js/api/Rendering_Core_Property.html). Each of those objects can be configured using the __actor__, __mapper__ and __property__ arguments of the __GeometryRepresentation__.

        The list below shows the default values for each argument:

        - __actor__:
            - origin = (0,0,0)
            - position = (0,0,0)
            - scale = (1,1,1)
            - visibility = 1
            - pickable = 1
            - dragable = 1
            - orientation = (0,0,0)
        - __property__:
            - lighting = true
            - interpolation = [Interpolation.GOURAUD](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Property/Constants.js#L1-L5)
            - ambient = 0
            - diffuse = 1
            - specular = 0
            - specularPower = 1
            - opacity = 1
            - edgeVisibility = false
            - lineWidth = 1
            - pointSize = 1
            - backfaceCulling = false
            - frontfaceCulling = false
            - representation = [Representation.SURFACE](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Property/Constants.js#L7-L11)
            - color = (1,1,1)          # White
            - ambientColor = (1,1,1)
            - specularColor = (1,1,1)
            - diffuseColor = (1,1,1)
            - edgeColor = (0,0,0)      # Black
        - __mapper__:
            - static = false
            - scalarVisibility = true
            - scalarRange = [0, 1]
            - useLookupTableScalarRange = false
            - colorMode = 0 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Mapper/Constants.js#L1-L5))
            - scalarMode = 0 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Mapper/Constants.js#L7-L14))
            - arrayAccessMode = 1 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Mapper/Constants.js#L16-L19))
            - colorByArrayName = ''
            - interpolateScalarsBeforeMapping = false
            - useInvertibleColors = false
            - fieldDataTupleId = -1
            - viewSpecificProperties = None
            - customShaderAttributes = []

        On top of those previous settings we provide additional properties to configure a lookup table using one of our available [__colorMapPreset__](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ColorTransferFunction/ColorMaps.json) and a convinient __colorDataRange__ to rescale to color map to your area of focus.

        With the GeometryRepresentation you also have the option to turn on the CubeAxes using the `showCubeAxes=True` along with additional configuration parameters that can be provided via the `cubeAxesStyle` property. The content of the object for __cubeAxesStyle__ can be found in the source code of vtk.js from the [default section here](https://github.com/Kitware/vtk-js/blob/HEAD/Sources/Rendering/Core/CubeAxesActor/index.js#L703-L719).

        ## GlyphRepresentation

        GlyphRepresentation lets you use a source as a Glyph which will then be cloned and positioned at every point of another source. The properties available on the __GlyphRepresentation__ let you tune the way you want to render your geometry.

        In VTK a representation is composed of an [__Actor__](https://kitware.github.io/vtk-js/api/Rendering_Core_Actor.html), a [__Mapper__](https://kitware.github.io/vtk-js/api/Rendering_Core_Glyph3DMapper.html) and a [__Property__](https://kitware.github.io/vtk-js/api/Rendering_Core_Property.html). Each of those objects can be configured using the __actor__, __mapper__ and __property__ arguments of the __GlyphRepresentation__.

        The list below shows the default values for each argument:

        - __actor__:
            - origin = (0,0,0)
            - position = (0,0,0)
            - scale = (1,1,1)
            - visibility = 1
            - pickable = 1
            - dragable = 1
            - orientation = (0,0,0)
        - __property__:
            - lighting = true
            - interpolation = [Interpolation.GOURAUD](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Property/Constants.js#L1-L5)
            - ambient = 0
            - diffuse = 1
            - specular = 0
            - specularPower = 1
            - opacity = 1
            - edgeVisibility = false
            - lineWidth = 1
            - pointSize = 1
            - backfaceCulling = false
            - frontfaceCulling = false
            - representation = [Representation.SURFACE](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Property/Constants.js#L7-L11)
            - color = (1,1,1)          # White
            - ambientColor = (1,1,1)
            - specularColor = (1,1,1)
            - diffuseColor = (1,1,1)
            - edgeColor = (0,0,0)      # Black
        - __mapper__:
            - orient = true
            - orientationMode = 0 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Glyph3DMapper/Constants.js#L1-L5))
            - orientationArray = null
            - scaling = true
            - scaleFactor = 1.0
            - scaleMode = 1 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Glyph3DMapper/Constants.js#L7-L11))
            - scaleArray = null
            - static = false
            - scalarVisibility = true
            - scalarRange = [0, 1]
            - useLookupTableScalarRange = false
            - colorMode = 0 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Mapper/Constants.js#L1-L5))
            - scalarMode = 0 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Mapper/Constants.js#L7-L14))
            - arrayAccessMode = 1 ([Available values](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/Mapper/Constants.js#L16-L19))
            - colorByArrayName = ''
            - interpolateScalarsBeforeMapping = false
            - useInvertibleColors = false
            - fieldDataTupleId = -1
            - viewSpecificProperties = None
            - customShaderAttributes = []

        On top of those previous settings we provide additional properties to configure a lookup table using one of our available [__colorMapPreset__](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ColorTransferFunction/ColorMaps.json) and a convinient __colorDataRange__ to rescale to color map to your area of focus.

        An example of the __GlyphRepresentation__ could be creating a spiky sphere by positioning cones normal to the sphere.

        ```python
        def Example():
            return dash_vtk.View(
            children=[
                dash_vtk.GlyphRepresentation(
                    mapper={'orientationArray': 'Normals'}
                    children=[
                        dash_vtk.Algorithm(
                            port=0,
                            vtkClass='vtkSphereSource',
                            state={
                                'phiResolution': 10,
                                'thetaResolution': 20,
                            },
                        ),
                        dash_vtk.Algorithm(
                            port=1,
                            vtkClass='vtkConeSource'
                            state={
                                'resolution': 30,
                                'height': 0.25,
                                'radius': 0.08,
                            },
                        ),
                    ]
                )
            ]
            )
        ```


        ## VolumeRepresentation

        The properties available on the __VolumeRepresentation__ let you tune the way you want to render your volume.

        In VTK a representation is composed of an [__Volume__](https://kitware.github.io/vtk-js/api/Rendering_Core_Volume.html), a [__Mapper__](https://kitware.github.io/vtk-js/api/Rendering_Core_VolumeMapper.html) and a [__Property__](https://kitware.github.io/vtk-js/api/Rendering_Core_VolumeProperty.html). Each of those objects can be configured using the __actor__, __mapper__ and __property__ arguments of the __GeometryRepresentation__.


        The list below shows the default values for each argument:

        - __volume__:
            - origin = (0,0,0)
            - position = (0,0,0)
            - scale = (1,1,1)
            - visibility = 1
            - pickable = 1
            - dragable = 1
            - orientation = (0,0,0)
        - __property__:
            - independentComponents = true
            - interpolationType = [InterpolationType.FAST_LINEAR](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/VolumeProperty/Constants.js#L1-L5)
            - shade = 0
            - ambient = 0.1
            - diffuse = 0.7
            - specular = 0.2
            - specularPower = 10.0
            - useLabelOutline = false
            - labelOutlineThickness = 1
            - useGradientOpacity = [idx, value]
            - scalarOpacityUnitDistance = [idx, value]
            - gradientOpacityMinimumValue = [idx, value]
            - gradientOpacityMinimumOpacity = [idx, value]
            - gradientOpacityMaximumValue = [idx, value]
            - gradientOpacityMaximumOpacity = [idx, value]
            - opacityMode = [idx, [value](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/VolumeProperty/Constants.js#L7-L10)]
        - __mapper__:
            - sampleDistance = 1.0
            - imageSampleDistance = 1.0
            - maximumSamplesPerRay = 1000
            - autoAdjustSampleDistances = true
            - blendMode = [BlendMode.COMPOSITE_BLEND](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/VolumeMapper/Constants.js#L1-L6)
            - averageIPScalarRange = [-1000000.0, 1000000.0]

        On top of those previous settings we provide additional properties to configure a lookup table using one of our available [__colorMapPreset__](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ColorTransferFunction/ColorMaps.json) and a convinient __colorDataRange__ to rescale to color map to your area of focus.

        Because it can be cumbersome and difficult to properly configure your volume rendering properties, it is convenient to add as first child to that representation a __VolumeController__ which will give you a UI to drive some of those parameters while also providing better defaults for your ImageData.

        ## VolumeController

        The __VolumeController__ provide a convenient UI element to control your Volume Rendering settings and can be tuned with the following set of properties:

        - __size__: [width, height] in pixel for the controller UI
        - __rescaleColorMap__: true/false to use the opacity piecewise function to dynamically rescale the color map or keep the full data range as color range.

        ## SliceRepresentation

        The __SliceRepresentation__ lets you see a slice within a 3D image. That slice can be along i,j,k or x,y,z if your volume contains an orientation matrix.

        The following set of properties lets you pick which slice you want to see. Only one of those properties can be used at a time.

        - __iSlice__, __jSlice__, __kSlice__: Index based slicing
        - __xSlice__, __ySlice__, __zSlice__: World coordinate slicing

        Then we have the standard representation set or properties with their defaults:

        - [__actor__](https://kitware.github.io/vtk-js/api/Rendering_Core_ImageSlice.html):
            - origin = (0,0,0)
            - position = (0,0,0)
            - scale = (1,1,1)
            - visibility = 1
            - pickable = 1
            - dragable = 1
            - orientation = (0,0,0)
        - [__property__](https://kitware.github.io/vtk-js/api/Rendering_Core_ImageProperty.html):
            - independentComponents = false
            - interpolationType = [InterpolationType.LINEAR](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ImageProperty/Constants.js#L1-L4)
            - colorWindow = 255
            - colorLevel = 127.5
            - ambient = 1.0
            - diffuse = 0.0
            - opacity = 1.0
        - [__mapper__](https://kitware.github.io/vtk-js/api/Rendering_Core_ImageMapper.html):
            - customDisplayExtent: [0, 0, 0, 0]
            - useCustomExtents: false
            - slice: 0
            - slicingMode: [SlicingMode.NONE](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ImageMapper/Constants.js#L1-L9)
            - closestIJKAxis: { ijkMode: [SlicingMode.NONE](https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ImageMapper/Constants.js#L1-L9), flip: false }
            - renderToRectangle: false
            - sliceAtFocalPoint: false

        ## PointCloudRepresentation

        The __PointCloudRepresentation__ is just a helper using the following structure to streamline rendering a point cloud dataset. The code snippet below is not complete but it should provide you with some understanding of the kind of simplification that is happening under the hood.

        ```python
        def PointCloudRepresentation(**kwargs):
            return dash_vtk.GeometryRepresentation(
                id=kwargs.get('id'),
                colorMapPreset=kwargs.get('colorMapPreset'),
                colorDataRange=kwargs.get('colorDataRange'),
                property=kwargs.get('property'),
                children=[
                dash_vtk.PolyData(
                    points=kwargs.get('xyz'),
                    connectivity='points',
                    children=[
                    dash_vtk.PointData([
                        dash_vtk.DataArray(
                        registration='setScalars',
                        values={kwargs.get('scalars')}
                        )
                    ])
                    ],
                )
                ],
            )
        ```

        The set of convenient properties are as follows:
        - __xyz__ = list of xyz of each point inside a flat array
        - __colorMapPreset__ = color preset name to use
        - __colorDataRange__ = rescale color map to provided that range
        - __property__ = {} # Same as GeometryRepresentation/property
        - __rgb__ / __rgba__ / __scalars__ = `[...]` let you define the field you want to color your point cloud with. The rgb(a) expects numbers up to 255 for each component: Red Green Blue (Alpha).

        ## VolumeDataRepresentation

        The __VolumeDataRepresentation__ is just a helper using the following structure to streamline rendering a volume. The code snippet below is not complete but it should provide you with some understanding of the kind of simplification that is happening under the hood.

        ```python
        def VolumeDataRepresentation(**kwargs):
        return dash_vtk.VolumeRepresentation(
            id=kwargs.get('id'),
            colorMapPreset=kwargs.get('colorMapPreset'),
            colorDataRange=kwargs.get('colorDataRange'),
            property=kwargs.get('property'),
            mapper=kwargs.get('mapper'),
            volume=kwargs.get('volume'),
            children=[
                dash_vtk.VolumeController(
                    rescaleColorMap=kwargs.get('rescaleColorMap'),
                    size=kwargs.get('size'),
                ),
                dash_vtk.ImageData(
                    dimensions=kwargs.get('dimensions'),
                    origin=kwargs.get('origin'),
                    spacing=kwargs.get('spacing'),
                    children=[
                        dash_vtk.PointData([
                            dash_vtk.DataArray(
                                registration='setScalars',
                                values=kwargs.get('scalars'),
                            )
                        ])
                    ],
                ),
                ],
            )
            ],
        )
        ```

        The set of convenient properties are as follows:
        - __dimensions__: Number of points along x, y, z
        - __spacing__: Spacing along x, y, z between points in world
        - __origin__: World coordinate of the lower left corner of your vtkImageData (i=0, j=0, k=0).
        - __rgb__: Use RGB values to attach to the points/vertex
        - __rgba__: Use RGBA values to attach to the points/vertex
        - __scalars__: Field values to attach to the points
        - __scalarsType__: Types of numbers provided in scalars (i.e. Float32Array, Uint8Array, ...)
        - __mapper__: Properties to set to the mapper
        - __volume__: Properties to set to the volume
        - __property__: Properties to set to the volume.property
        - __colorMapPreset__: Preset name for the lookup table color map
        - __volumeController__: Show volumeController
        - __controllerSize__: Controller size in pixels
        - __rescaleColorMap__: Use opacity range to rescale color map
        '''
    )
])
