## Storing annotations in a dcc.Store component

When building a training set for deep learning, or in other applications, one needs to store and save image annotations for future use. This can be done using a`dcc.Store` component.

The example implements an image carousel where annotations are stored for each image. When the sequence comes back to a previously annotated image, annotations are read from the store and displayed as layout shapes on the image.
