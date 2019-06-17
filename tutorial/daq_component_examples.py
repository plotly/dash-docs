# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent as s

from tutorial import styles
from tutorial import tools
from tutorial.utils.convert_props_to_table_daq import generate_prop_table
from tutorial.utils.component_block import ComponentBlock
from tutorial.components import Syntax, Example

examples = {
    'boolean-switch': tools.load_example('tutorial/examples/daq_components/boolean_switch.py'),
    'color-picker': tools.load_example('tutorial/examples/daq_components/color_picker.py'),
    'gauge': tools.load_example('tutorial/examples/daq_components/gauge.py'),
    'graduated-bar': tools.load_example('tutorial/examples/daq_components/graduated_bar.py'),
    'indicator': tools.load_example('tutorial/examples/daq_components/indicator.py'),
    'knob': tools.load_example('tutorial/examples/daq_components/knob.py'),
    'LED-display': tools.load_example('tutorial/examples/daq_components/LED_display.py'),
    'numeric-input': tools.load_example('tutorial/examples/daq_components/numeric_input.py'),
    'power-button': tools.load_example('tutorial/examples/daq_components/power_button.py'),
    'precision-input': tools.load_example('tutorial/examples/daq_components/precision_input.py'),
    'stop-button': tools.load_example('tutorial/examples/daq_components/stop_button.py'),
    'slider': tools.load_example('tutorial/examples/daq_components/slider.py'),
    'tank': tools.load_example('tutorial/examples/daq_components/tank.py'),
    'thermometer': tools.load_example('tutorial/examples/daq_components/thermometer.py'),
    'toggle-switch': tools.load_example('tutorial/examples/daq_components/toggle_switch.py'),
    'dark-theme-provider': tools.load_example('tutorial/examples/daq_components/dark_theme_provider.py'),
    'joystick': tools.load_example('tutorial/examples/daq_components/joystick.py')
}


# BooleanSwitch
BooleanSwitch = html.Div(children=[
    html.H1('Boolean Switch Examples and Reference'),
    html.Hr(),
    html.H3('Default Boolean Switch'),
    html.P("An example of a default boolean switch without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['boolean-switch'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['boolean-switch'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Color'),
    dcc.Markdown("Set the color of the boolean switch with \
    `color=#<hex_value>`."),
    ComponentBlock('''import dash_daq as daq

daq.BooleanSwitch(
  on=True,
  color="#9B51E0",
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Label'),
    dcc.Markdown("Set the label and label position using the `label` and `labelPosition` \
    properties."),
    ComponentBlock('''import dash_daq as daq

daq.BooleanSwitch(
  on=True,
  label="Label",
  labelPosition="top"
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Vertical Switch'),
    dcc.Markdown("Create a vertical oriented switch by setting `vertical=True`."),
    ComponentBlock('''import dash_daq as daq

daq.BooleanSwitch(
  on=True,
  label="Vertical",
  vertical=True
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Disabled Switch'),
    dcc.Markdown("To disable the Boolean Switch set the property `disabled` to `True`."),
    ComponentBlock('''import dash_daq as daq

daq.BooleanSwitch(
  disabled=True,
  label="Disabled",
  labelPosition="bottom"
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Boolean Switch Properties"),
    generate_prop_table('BooleanSwitch')
])

# ColorPicker
ColorPicker = html.Div(children=[
    html.H1('Color Picker Examples and Reference'),
    html.Hr(),
    html.H3('Default Color Picker'),
    html.P("An example of a default Color Picker without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['color-picker'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['color-picker'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Set the size (width) of the color picker in pixels using the `size` property."),
    ComponentBlock('''import dash_daq as daq

daq.ColorPicker(
  label="Small",
  size=164,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Label'),
    dcc.Markdown("Define the label and label position using the `label` and `labelPosition` \
    properties."),
    ComponentBlock('''import dash_daq as daq

daq.ColorPicker(
  label="Label",
  labelPosition="bottom"
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
html.H3('Disabled'),
    dcc.Markdown("To disable the Color Picker set `disabled` to `True`."),
    ComponentBlock('''import dash_daq as daq

daq.ColorPicker(
  label='Color Picker',
  disabled=True,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
html.H3('Hex Colors'),
    dcc.Markdown("Use hex values with the Color Picker by setting `value=dict(hex='#<hex_color>')`"),
    ComponentBlock('''import dash_daq as daq

daq.ColorPicker(
  label='Color Picker',
  value=dict(hex="#0000FF"),
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
html.H3('RGB Colors'),
    dcc.Markdown("Use RGB color values with the Color Picker by setting: \
    \n `value=(rgb=dict(r=<r_value>, g=<g_value>, b=<b_value>, a=<a_value>)`"),
    ComponentBlock('''import dash_daq as daq

daq.ColorPicker(
label='Color Picker',
value=dict(rgb=dict(r=255, g=0, b=0, a=0))
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.Hr(),
    html.H3("Color Picker Properties"),
    generate_prop_table('ColorPicker')
])

# Gauge
Gauge = html.Div(children=[
    html.H1('Gauge Examples and Reference'),
    html.Hr(),
    html.H3('Default Gauge'),
    html.P("An example of a default Gauge without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['gauge'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['gauge'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Minimum and Maximum'),
    dcc.Markdown("Specify the minimum and maximum values of the gauge, using the `min` and `max` properties. If \
    the scale is logarithmic the minimum and maximum will represent an exponent."),
    ComponentBlock('''import dash_daq as daq

daq.Gauge(
    value=5,
    label='Default',
    max=20,
    min=0,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Current Value and Units'),
    dcc.Markdown("Show the current value of the gauge and the units with `showCurrentValue=True` \
    and `units=<units>`."),
    ComponentBlock('''import dash_daq as daq

daq.Gauge(
    showCurrentValue=True,
    units="MPH",
    value=5,
    label='Default',
    max=10,
    min=0,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Logarithmic Gauge'),
    dcc.Markdown("To set the scale of the gauge to logarithmic use the property `logarithmic=True`."),
    ComponentBlock('''import dash_daq as daq

daq.Gauge(
    logarithmic=True,
    value=5,
    label='Default',
    max=10,
    min=0,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color'),
    dcc.Markdown("Set the color of the gauge by using the property `color=<hex_color>`."),
    ComponentBlock('''import dash_daq as daq

daq.Gauge(
    color="#9B51E0",
    value=2,
    label='Default',
    max=5,
    min=0,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color Gradient'),
    dcc.Markdown("Apply a color gradient to the gauge with the property: \
    \n `color={'gradient':True,'ranges':{'<color>':[<value>, <value>],'<color>':[<value>, <value>],'<color>':[<value>, <value>]}}`."),
    ComponentBlock('''import dash_daq as daq

daq.Gauge(
    color={"gradient":True,"ranges":{"green":[0,6],"yellow":[6,8],"red":[8,10]}},
    value=2,
    label='Default',
    max=10,
    min=0,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Adjust the size of the gauge in pixels `size=200`."),
    ComponentBlock('''import dash_daq as daq

daq.Gauge(
    size=200,
    value=2,
    label='Default',

)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Scale'),
    dcc.Markdown("Modify where the scale starts, the label interval, and actual interval \
    with the `scale` property."),
    ComponentBlock('''import dash_daq as daq

daq.Gauge(
  label='Scale',
  scale={'start': 0, 'interval': 3, 'labelInterval': 2},
  value=3,
  min=0,
  max=24,
)''' , customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Gauge Properties"),
    generate_prop_table('Gauge')
])

# Graduated Bar
GraduatedBar = html.Div(children=[
    html.H1('Graduated bar Examples and Reference'),
    html.Hr(),
    html.H3('Default Graduated bar'),
    dcc.Markdown("An example of a default Graduated bar without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['graduated-bar'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['graduated-bar'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),
    html.Hr(),
    html.H3('Orientation'),
    dcc.Markdown("Change the orientation of the bar to vertical `vertical=True`."),
    ComponentBlock('''import dash_daq as daq

daq.GraduatedBar(
    vertical=True,
    value=10
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Manually adjust the size of the bar in pixels with `size`."),
    ComponentBlock('''import dash_daq as daq

daq.GraduatedBar(
    size=200,
    value=10
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Max'),
    dcc.Markdown("Manually set a maximum value with `max`."),
    ComponentBlock('''import dash_daq as daq

daq.GraduatedBar(
    max=100,
    value=50
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Step'),
    dcc.Markdown("Manually set the step size of each bar with `step`."),
    ComponentBlock('''import dash_daq as daq

daq.GraduatedBar(
    step=2,
    max=100,
    value=50
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Show Current Value'),
    dcc.Markdown("Display the current value of the graduated bar with `showCurrentValue=True`."),
    ComponentBlock('''import dash_daq as daq

daq.GraduatedBar(
    showCurrentValue=True,
    max=100,
    value=38
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color Range'),
    dcc.Markdown("Set a color range with:  \
    \n `color={'ranges':{'<color>':[<value>, <value>],'<color>':[<value>, <value>],'<color>':[<value>, <value>]}}`"),
    ComponentBlock('''import dash_daq as daq

daq.GraduatedBar(
    color={"ranges":{"green":[0,4],"yellow":[4,7],"red":[7,10]}},
    showCurrentValue=True,
    value=10
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color Gradient'),
    dcc.Markdown("Set a color gradient with: \
    \n `color={'gradient':{'<color>':[<value>, <value>],'<color>':[<value>, <value>],'<color>':[<value>, <value>]}}`"),
    ComponentBlock('''import dash_daq as daq

daq.GraduatedBar(
    color={"gradient":True,"ranges":{"green":[0,4],"yellow":[4,7],"red":[7,10]}},
    showCurrentValue=True,
    value=10
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Graduated Bar Properties"),
    generate_prop_table('GraduatedBar')
])

# Indicator
Indicator = html.Div(children=[
    html.H1('Indicator Examples and Reference'),
    html.Hr(),
    html.H3('Default Indicator'),
    dcc.Markdown("An example of a default Indicator without \
        any extra properties."),
    dcc.SyntaxHighlighter(
        examples['indicator'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['indicator'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Label'),
    dcc.Markdown(
        "Define the label and label orientation with `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq

daq.Indicator(
  label="Label",
  labelPosition="bottom",
  value=True
)''', customStyle=styles.code_container, language='python'),
    html.H3('Boolean Indicator Off'),
    dcc.Markdown("A boolean indicator set to off `value=False`."),
    ComponentBlock('''import dash_daq as daq

daq.Indicator(
  label="Off",
  value=False
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Square'),
    dcc.Markdown("Create a square boolean indicator by setting the \
    `width` and `height` to the same value."),
    ComponentBlock('''import dash_daq as daq

daq.Indicator(
  label="Square",
  width=16,
  height=16
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color'),
    dcc.Markdown(
        "Define the color of the boolean indicator with `color='#<color>'`"),
    ComponentBlock('''import dash_daq as daq

daq.Indicator(
  label="Purple",
  color="#551A8B",
  value=True
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Indicator Properties"),
    generate_prop_table('Indicator')
])

# Joystick
Joystick = html.Div(children=[
    html.H1('Joystick Examples and Reference'),
    html.Hr(),
    html.H3('Default Joystick'),
    dcc.Markdown("An example of a default Joystick without \
    any extra properties."),
    dcc.SyntaxHighlighter(
        examples['joystick'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['joystick'][1],
        style={'overflow=x': 'initial'}
    ),

    html.Hr(),
    html.H3('Label'),
    dcc.Markdown(
        "Change the label and label orientation with `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq

daq.Joystick(
  label="Label",
  labelPosition="bottom"
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),
    html.H3('Size'),
    dcc.Markdown(
        "Change the size of the joystick with `size`."),
    ComponentBlock('''import dash_daq as daq

daq.Joystick(
  size=250
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Joystick Properties'),
    generate_prop_table('Joystick')
])

# Knob
Knob = html.Div(children=[
    html.H1('Knob Examples and Reference'),
    html.Hr(),
    html.H3('Default Knob'),
    dcc.Markdown("An example of a default Knob without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['knob'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['knob'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Set the size(diameter) of the knob in pixels with `size`."),
    ComponentBlock('''import dash_daq as daq

daq.Knob(
    size=140,
    value=3
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Max'),
    dcc.Markdown("Set the maximum value of the knob using `max`."),
    ComponentBlock('''import dash_daq as daq

daq.Knob(
    max=100,
    value=3
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color Ranges'),
    dcc.Markdown("Control color ranges with: \
    \n `color={'ranges':{'<color>':[<value>,<value>],'<color>':[<value>,<value>], '<color>':[<value>,<value>]}}`."),
    ComponentBlock('''import dash_daq as daq

daq.Knob(
  label="Color Ranges",
  value=3,
  color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}}
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color Gradient'),
    dcc.Markdown("Set up a color gradient with: \
    \n `color={'ranges':{'gradient': True,'ranges' <color>':[<value>,<value>],'<color>':[<value>,<value>], '<color>':[<value>,<value>]}}`."),
    ComponentBlock('''import dash_daq as daq

daq.Knob(
  label="Gradient Ranges",
  value=7,
  color={"gradient":True,"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}}
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Scale'),
    dcc.Markdown("Adjust the scale interval, label interval, \
    and start of the scale with `scale`."),
    ComponentBlock('''import dash_daq as daq

daq.Knob(
  label="Gradient Ranges",
  value=7,
  max=18,
  scale={'start':0, 'labelInterval': 3, 'interval': 3}
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Knob Properties"),
    generate_prop_table('Knob')
])

# LED Display
LEDDisplay = html.Div(children=[
    html.H1('LED display Examples and Reference'),
    html.Hr(),
    html.H3('Default LED display'),
    dcc.Markdown("An example of a default LED display without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['LED-display'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['LED-display'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Label'),
    dcc.Markdown("Set the label and label position with \
    `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq

daq.LEDDisplay(
    label="Label",
    labelPosition='bottom',
    value='12:34'
)''', customStyle=styles.code_container, language='python'),
    html.H3('Size'),
    dcc.Markdown("Adjust the size of the LED display with `size`"),
    ComponentBlock('''import dash_daq as daq

daq.LEDDisplay(
    label="Large",
    value="9:34",
    size=64,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Color'),
    dcc.Markdown("Adjust the color of the LED display with `color=#<hex_color>`"),
    ComponentBlock('''import dash_daq as daq

daq.LEDDisplay(
    label="color",
    value='1.001',
    color="#FF5E5E"
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Background Color'),
    dcc.Markdown("Adjust the background color of the LED display using: \
    \n `backgroundColor=#<hex_color>`"),
    ComponentBlock('''import dash_daq as daq

daq.LEDDisplay(
    label="color",
    value='1.001',
    backgroundColor="#FF5E5E"
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("LED Display Properties"),
    generate_prop_table('LEDDisplay')
])

# Numeric Input
NumericInput = html.Div(children=[
    html.H1('Numeric Input Examples and Reference'),
    html.Hr(),
    html.H3('Default Numeric Input'),
    dcc.Markdown("An example of a default numeric input without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['numeric-input'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['numeric-input'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),
    html.Hr(),
    html.H3('Label'),
    dcc.Markdown("Set the label and label position with \
    `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq

daq.NumericInput(
    label='Label',
    labelPosition='bottom',
    value=10,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Extend the size with `size`."),
    ComponentBlock('''import dash_daq as daq

daq.NumericInput(
    value=10,
    size=120
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Max and Min'),
    dcc.Markdown("Set the minimum and maximum bounds with `min` and max`."),
    ComponentBlock('''import dash_daq as daq

daq.NumericInput(
    min=0,
    max=100,
    value=20
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Disable'),
    dcc.Markdown("Disable the numeric input by setting `disabled=True`."),
    ComponentBlock('''import dash_daq as daq

daq.NumericInput(
    disabled=True,
    min=0,
    max=10,
    value=2
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.Hr(),
    html.H3("Numeric Input Properties"),
    generate_prop_table('NumericInput')
])

# Power Button
PowerButton = html.Div(children=[
    html.H1('Power Button Examples and Reference'),
    html.Hr(),
    html.H3('Default Power Button'),
    dcc.Markdown("An example of a default power button without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['power-button'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['power-button'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Label'),
    dcc.Markdown("Set the label and label position with `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq

daq.PowerButton(
    on='True',
    label='Label',
    labelPosition='top'
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Adjust the size (diameter in pixels) of the power button with `size`."),
    ComponentBlock('''import dash_daq as daq

daq.PowerButton(
    on='True',
    size=100
)''', customStyle=styles.code_container, language='python'),
    html.H3('Color'),
    dcc.Markdown("Set the color of the power button with `color`."),
    ComponentBlock('''import dash_daq as daq

daq.PowerButton(
    on='True',
    color='#FF5E5E'
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Power Button Properties"),
    generate_prop_table('PowerButton')
])

# Precision Input
PrecisionInput = html.Div(children=[
    html.H1('Precision Input Examples and Reference'),
    html.Hr(),
    html.H3('Default Precision Input'),
    dcc.Markdown("An example of a default precision input without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['precision-input'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['precision-input'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),
    html.Hr(),
    html.H3('Label'),
    dcc.Markdown("Set the label and label position with `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq

daq.PrecisionInput(
    label='Label',
    labelPosition='top',
    precision=2,
    value=12
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Precision'),
    dcc.Markdown("The `precision` property is mandatory for this component. The `precision` property \
    indicates the accuracy of the specified number."),
    ComponentBlock('''import dash_daq as daq

daq.PrecisionInput(
    precision=2,
    value=125
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Max and Min'),
    dcc.Markdown("Set the maximum and minimum value of the numeric input with `max` and `min`."),
    ComponentBlock('''import dash_daq as daq

daq.PrecisionInput(
    precision=2,
    value=15,
    max=20,
    min=10
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Set the length (in pixels) of the numeric input `size`."),
    ComponentBlock('''import dash_daq as daq

daq.PrecisionInput(
    size=120,
    precision=4,
    value=245
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Disabled'),
    dcc.Markdown("Disable the precision input by setting `disabled=True`."),
    ComponentBlock('''import dash_daq as daq

daq.PrecisionInput(
    disabled=True,
    precision=4,
    value=9999
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Precision Input Properties"),
    generate_prop_table('PrecisionInput')
])

# Stop Button
StopButton = html.Div(children=[
    html.H1('Stop Button Examples and Reference'),
    html.Hr(),
    html.H3('Default Stop Button'),
    dcc.Markdown("An example of a default stop button without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['stop-button'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['stop-button'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),
    html.H3('Label'),
    dcc.Markdown("Set the label and label position with `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq

daq.StopButton(
    label='Label',
    labelPosition='top'
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Size'),
    dcc.Markdown("Adjust the size (width in pixels) of the stop button with `size`."),
    ComponentBlock('''import dash_daq as daq

daq.StopButton(
    size=120,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Button Text'),
    dcc.Markdown("Set the text displayed in the button `buttonText`."),
    ComponentBlock('''import dash_daq as daq

daq.StopButton(
    buttonText='text',
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3('Disabled'),
    dcc.Markdown("Disable the button by setting `disabled=True`."),
    ComponentBlock('''import dash_daq as daq

daq.StopButton(
    disabled=True,
)''', customStyle=styles.code_container, language='python'),
    html.Hr(),
    html.H3("Stop Button Properties"),
    generate_prop_table('StopButton')
])

# Slider
Slider = html.Div(children=[
    html.H1('Slider Examples and Reference'),
    html.Hr(),
    html.H3('Default Slider'),
    dcc.Markdown("An example of a default slider without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['slider'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['slider'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),

    html.H3('Marks'),
    dcc.Markdown("Set custom marks on the slider using with `marks`."),
    ComponentBlock('''import dash_daq as daq
daq.Slider(
    min=0, max=100, value=30,
    marks={'25': 'mark', '50': '50'}
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Size'),
    dcc.Markdown("Change the size of the slider using `size`."),
    ComponentBlock('''import dash_daq as daq
daq.Slider(
    size=50
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Handle Label'),
    dcc.Markdown("Set the labels for the handle that is dragged with `handleLabel`."),
    ComponentBlock('''import dash_daq as daq

daq.Slider(
    id='my-daq-slider',
    value=17,
    handleLabel='Handle'
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Step'),
    dcc.Markdown("Change the value of increments or decrements using `step`."),
    ComponentBlock('''import dash_daq as daq
daq.Slider(
    min=0,
    max=100,
    value=50,
    handleLabel={"showCurrentValue": True,"label": "VALUE"},
    step=10
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Vertical orientation'),
    dcc.Markdown("Make the slider display vertically by setting `vertical=True`."),
    ComponentBlock('''import dash_daq as daq
daq.Slider(
    vertical=True
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3("Slider Properties"),
    generate_prop_table("Slider")

])

# Tank
Tank = html.Div(children=[
    html.H1('Tank Examples and Reference'),
    html.Hr(),
    html.H3('Default Tank'),
    dcc.Markdown("An example of a default tank without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['tank'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['tank'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),

    html.H3('Current value with units'),
    dcc.Markdown("Display the current value, along with optional \
    units with the `units` and `showCurrentValue` properties."),
    ComponentBlock('''import dash_daq as daq
daq.Tank(
    value=6,
    showCurrentValue=True,
    units='gallons',
    style={'margin-left': '50px'}
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Size') ,
    dcc.Markdown("Control the height of the tank by setting `size`."),
    ComponentBlock('''import dash_daq as daq
daq.Tank(
    size=100,
    value=6,
    style={'margin-left': '50px'}
)
''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Label'),
    dcc.Markdown("Display a label alongside your tank in the \
    specified position with `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq
daq.Tank(
    value=3,
    label='Tank label',
    labelPosition='bottom'
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Custom scales'),
    dcc.Markdown("Control the intervals at which labels are displayed, \
    as well as the labels themselves with the `scale` property."),
    ComponentBlock('''import dash_daq as daq
daq.Tank(
    value=3,
    scale={'interval': 2, 'labelInterval': 2,
           'custom': {'5': 'Set point'}},
    style={'margin-left': '50px'}
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Logarithmic'),
    dcc.Markdown("Use a logarithmic scale for the tank with the specified \
    base by setting `logarithmic=True`."),
    ComponentBlock('''import dash_daq as daq
daq.Tank(
    min=0,
    max=10,
    value=300,
    logarithmic=True,
    base=3,
    style={'margin-left': '50px'}
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Tank Properties'),
    generate_prop_table("Tank")
])

# Thermometer
Thermometer = html.Div(children=[
    html.H1('Thermometer Examples and Reference'),
    html.Hr(),
    html.H3('Default Thermometer'),
    dcc.Markdown("An example of a default Thermometer without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['thermometer'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['thermometer'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),

    html.H3('Current value with units'),
    dcc.Markdown("Display the value of the thermometer along with \
    optional units with ` showCurrentValue` and `units`."),
    ComponentBlock('''import dash_daq as daq
daq.Thermometer(
    min=95,
    max=105,
    value=100,
    showCurrentValue=True,
    units="C"
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Size'),
    dcc.Markdown("Control the size of the thermometer using `size`."),
    ComponentBlock('''import dash_daq as daq
daq.Thermometer(
    value=5,
    size=100
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Label'),
    dcc.Markdown("Display a label alongside the thermometer in \
    the specified positon by setting `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq
daq.Thermometer(
    value=5,
    label='Current temperature',
    labelPosition='top'
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Custom scales'),
    dcc.Markdown("Control the intervals at which labels are displayed, \
    as well as the labels themselves with the `scale` property."),
    ComponentBlock('''import dash_daq as daq
daq.Thermometer(
    value=5,
    scale={'start': 2, 'interval': 3,
    'labelInterval': 2, 'custom': {
        '2': 'ideal temperature',
        '5': 'projected temperature'
    }}
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Thermometer Properties'),
    generate_prop_table("Thermometer")

])

# Toggle Switch
ToggleSwitch = html.Div(children=[
    html.H1('Toggle Switch Examples and Reference'),
    html.Hr(),
    html.H3('Default Toggle Switch'),
    dcc.Markdown("An example of a default toggle switch without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['toggle-switch'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['toggle-switch'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),

    html.H3('Vertical orientation'),
    dcc.Markdown("Make the switch display vertically by setting `vertical=True`."),
    ComponentBlock('''import dash_daq as daq
daq.ToggleSwitch(
    vertical=True
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Size'),
    dcc.Markdown("Adjust the size of the toggle switch with `size`."),
    ComponentBlock('''import dash_daq as daq
daq.ToggleSwitch(
    size=100
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Label'),
    dcc.Markdown("Add a label to the toggle switch and specify \
    its position using `label` and `labelPosition`."),
    ComponentBlock('''import dash_daq as daq
daq.ToggleSwitch(
    label='My toggle switch',
    labelPosition='bottom'
)''', customStyle=styles.code_container, language='python'),

    html.Hr(),

    html.H3('Toggle Switch Properties'),
    generate_prop_table("ToggleSwitch")

])

# Dark Theme Provider
DarkThemeProvider = html.Div(children=[
    html.H1('Dark Theme Provider Examples and Reference'),
    html.Hr(),
    html.H3('Default Dark Theme Provider'),
    dcc.Markdown("An example of a default dark theme provider without \
            any extra properties."),
    dcc.SyntaxHighlighter(
        examples['dark-theme-provider'][0],
        customStyle=styles.code_container
    ),
    html.Div(
        examples['dark-theme-provider'][1],
        className='example-container',
        style={'overflow-x': 'initial'}
    ),

    html.Hr(),

    html.H3('Dark Theme Provider Properties'),
    generate_prop_table("DarkThemeProvider")
])
