'''
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/. */
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
<!-- This Source Code Form is subject to the terms of the Mozilla Public
   - License, v. 2.0. If a copy of the MPL was not distributed with this
   - file, You can obtain one at https://mozilla.org/MPL/2.0/. -->
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
'''
import math
from discord_components import Button, ButtonStyle

buttons = [
    [
        Button(style=ButtonStyle.grey, label="1"),
        Button(style=ButtonStyle.grey, label="2"),
        Button(style=ButtonStyle.grey, label="3"),
        Button(style=ButtonStyle.blue, label="×"),
        Button(style=ButtonStyle.red, label="Exit"),
    ],
    [
        Button(style=ButtonStyle.grey, label="4"),
        Button(style=ButtonStyle.grey, label="5"),
        Button(style=ButtonStyle.grey, label="6"),
        Button(style=ButtonStyle.blue, label="÷"),
        Button(style=ButtonStyle.red, label="←"),
    ],
    [
        Button(style=ButtonStyle.grey, label="7"),
        Button(style=ButtonStyle.grey, label="8"),
        Button(style=ButtonStyle.grey, label="9"),
        Button(style=ButtonStyle.blue, label="+"),
        Button(style=ButtonStyle.red, label="Clear"),
    ],
    [
        Button(style=ButtonStyle.grey, label="00"),
        Button(style=ButtonStyle.grey, label="0"),
        Button(style=ButtonStyle.grey, label="."),
        Button(style=ButtonStyle.blue, label="-"),
        Button(style=ButtonStyle.green, label="="),
    ],
    [
        Button(style=ButtonStyle.grey, label="("),
        Button(style=ButtonStyle.grey, label=")"),
        Button(style=ButtonStyle.grey, label="π"),
        Button(style=ButtonStyle.grey, label="x²"),
        Button(style=ButtonStyle.grey, label="x³"),
    ],
]


def calculate(exp):
    o = exp.replace("×", "*")
    o = o.replace("÷", "/")
    o = o.replace("π", str(math.pi))
    o = o.replace("²", "**2")
    o = o.replace("³", "**3")
    result = ""
    try:
        result = str(eval(o))

    except BaseException:
        result = "An error occurred."

    return result