# streamlit-toggle-diy

Creates a toggle switch with color and placement customizations, and you can change the label's color, radius, font size, and more.

## Function

- Customize label background color
- Customize the text color, font size, and font weight for both labels
- Customize the Switch size (small or medium)
- Customize the background color near the button
- Custom rounded corners
- Support multiple layout methods

## Installation

```shell
pip install streamlit-toggle-diy
```

## Usage

```python
import streamlit as st
import streamlit-toggle-diy as tog

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

## Parameters


| **Parameter Name**                         | **Type**                             | **Default**    | **Description**                                                                                                                         |
| ------------------------------------------ | ------------------------------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **key**                                    | `str`                                | None           | The unique identifier for each component instance.<br />Used to distinguish different component instances in the Streamlit application. |
| **label\_start**                           | `str`                                | `""`           | The text content of the label before the switch. If a preceding label is not needed, pass an empty string`""`.                          |
| **label\_end**                             | `str`                                | `""`           | The text content of the label after the switch. If a following label is not needed, pass an empty string`""`.                           |
| **justify**                                | `{'flex-start','center','flex-end'}` | `'flex-start'` | Controls alignment of labels and the switch within the container.                                                                       |
| **default\_value**                         | `bool`                               | `False`        | The initial state of the toggle switch.`True`= On,`False`= Off.                                                                         |
| **inactive\_color**                        | `str`                                | `'#D3D3D3'`    | The color of the slider when the switch is inactive (off).                                                                              |
| **active\_color**                          | `str`                                | `'#11567f'`    | The color of the slider when the switch is active (on).                                                                                 |
| **track\_color**                           | `str`                                | `'#29B5E8'`    | The color of the switch track (background).                                                                                             |
| **label\_bg\_color\_start**                | `str`                                | `None`         | The starting value of the label background color, used to create a gradient effect.                                                     |
| **label\_bg\_color\_end**                  | `str`                                | `None`         | The ending value of the label background color, used to create a gradient effect.                                                       |
| **background\_color\_near\_button\_start** | `str`                                | `None`         | The starting value of the background color near the switch, used to create a gradient effect behind the component.                      |
| **background\_color\_near\_button\_end**   | `str`                                | `None`         | The ending value of the background color near the switch, used to create a gradient effect behind the component.                        |
| **border\_radius**                         | `str`                                | `None`         | The border-radius of the component, such as`'4px'`,`'8px'`,`'50%'`, etc.                                                                |
| **label\_start\_color**                    | `str`                                | `"#7f1916"`    | Text color for the left (start) label.                                                                                                  |
| **label\_end\_color**                      | `str`                                | `"#FFFFFF"`    | Text color for the right (end) label.                                                                                                   |
| **label\_font\_size**                      | `str`                                | `"14px"`       | Font size for both labels (e.g.`"14px"`,`"12pt"`).                                                                                      |
| **label\_font\_weight**                    | `str`                                | `"bold"`       | Font weight for both labels (e.g.`"bold"`,`"normal"`,`"500"`).                                                                          |
| **switch\_size**                           | `{'small','medium'}`                 | `"medium"`     | The size of the Switch component.                                                                                                       |

> **Note**:
>
> * If both `label_bg_color_start` and `label_bg_color_end` are set, a gradient background for the label(s) will be created.
> * If both `background_color_near_button_start` and `background_color_near_button_end` are provided, a gradient behind the switch is created.
> * If you only provide one color, it will be used as a solid background.
> * `label_start_color` and `label_end_color` control the text color of labels, while `label_bg_color_start` and `label_bg_color_end` control the background of those labels.

## Operation

![streamlit.gif](assets/streamlit.gif)
