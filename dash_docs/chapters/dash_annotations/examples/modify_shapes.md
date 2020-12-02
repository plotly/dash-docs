## Modifying shapes and parsing `relayoutData`

When adding a new shape, the `relayoutData` variable consists in the list of all layout shapes. It is also possible to delete a shape by selecting an existing shape, and by clicking the "delete shape" button in the modebar.

Also, existing shapes can be modified if their `editable` property is set to True. In the example below, you can
- draw a shape
- then click on the shape perimeter to select the shape
- drag one of its vertices to modify the shape

Observe that when modifying the shape, only the modified geometrical parameters are found in the `relayoutData`.

