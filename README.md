# streamlit_toggle_switch_diy

Creates a toggle switch with color and placement customizations, and you can change the label's color and radius.

## Function

- Customize label background color
- Customize the background color near the button
- Custom rounded corners
- Support multiple layout methods

## Installation

```shell
pip install streamlit-toggle-switch-diy
```

## Usage

```python
import streamlit as st
import streamlit_toggle_diy as tog

tog.st_toggle_switch(
        key=None,
        label_start="111",  
        label_end="",   
        justify='flex-start',
        default_value=False,
        inactive_color='#D3D3D3',
        active_color="#11567f",
        track_color="#29B5E8",
        label_bg_color_start=None,
        label_bg_color_end=None,
        background_color_near_button_start=None,
        background_color_near_button_end=None,
        border_radius=None,
                     )
```

## Parameter


| **Parameter Name**                   | **Type** | **Description**                                                                                                                                                                 |
| ------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `label`                              | `str`    | The main label of the component, used to identify the function of the switch.                                                                                                   |
| `key`                                | `str`    | The unique identifier for each component instance. <br />Used to distinguish different component instances in the Streamlit application.                                        |
| `default_value`                      | `bool`   | The initial state of the toggle switch.`True`indicates on,`False`indicates off.                                                                                                 |
| `label_start`                        | `str`    | The text content of the label before the switch. If a preceding label is not needed, an empty string`""`can be passed.                                                          |
| `label_end`                          | `str`    | The text content of the label after the switch. If a following label is not needed, an empty string`""`can be passed.                                                           |
| `justify`                            | `str`    | Controls the alignment of labels and switches within the container. Optional values include`'flex-start'`(left-aligned),`'center'`(center-aligned),`'flex-end'`(right-aligned). |
| `inactive_color`                     | `str`    | The color of the slider when the switch is inactive (off).                                                                                                                      |
| `active_color`                       | `str`    | The color of the slider when the switch is active (on).                                                                                                                         |
| `track_color`                        | `str`    | The color of the switch track (background).                                                                                                                                     |
| `label_bg_color_start`               | `str`    | The starting value of the label background color, used to create a gradient effect.                                                                                             |
| `label_bg_color_end`                 | `str`    | The ending value of the label background color, used to create a gradient effect.                                                                                               |
| `background_color_near_button_start` | `str`    | The starting value of the background color near the switch, used to create a gradient effect.                                                                                   |
| `background_color_near_button_end`   | `str`    | The ending value of the background color near the switch, used to create a gradient effect.                                                                                     |
| `border_radius`                      | `str`    | The border radius value of the component, such as`'4px'`,`'8px'`,`'50%'`, etc.                                                                                                  |


## Operation

![streamlit.gif](assets/streamlit.gif)
