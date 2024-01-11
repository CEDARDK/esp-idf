# SPDX-FileCopyrightText: 2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0

import os
import sys
from pathlib import Path

tools_ci_dir = os.path.join(os.path.dirname(__file__), '..', '..')
if tools_ci_dir not in sys.path:
    sys.path.append(tools_ci_dir)

tools_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')
if tools_dir not in sys.path:
    sys.path.append(tools_dir)


def create_project(name: str, folder: Path) -> Path:
    p = folder / name
    p.mkdir(parents=True, exist_ok=True)
    (p / 'main').mkdir(parents=True, exist_ok=True)

    with open(p / 'CMakeLists.txt', 'w') as fw:
        fw.write(
            """cmake_minimum_required(VERSION 3.16)
include($ENV{{IDF_PATH}}/tools/cmake/project.cmake)
project({})
""".format(
                name
            )
        )

    with open(p / 'main' / 'CMakeLists.txt', 'w') as fw:
        fw.write(
            """idf_component_register(SRCS "{}.c"
INCLUDE_DIRS ".")
""".format(
                name
            )
        )

    with open(p / 'main' / f'{name}.c', 'w') as fw:
        fw.write(
            """#include <stdio.h>
void app_main(void) {}
"""
        )

    return p
