#! /usr/bin/env python

from typing import Any, Optional

import click
from click import Context
from ni.core.commands.common import COMMON_COMMANDS


default_map = {
    "runserver": {"port": 9000},
    "runtests": {
        "test_folder": "tests/",
        "cover_package": ["app.routers", "app.helpers"],
    },
}



@click.group()
@click.option("--dev", is_flag=True, default=False)
def cli(dev: bool) -> None:
    ...


@cli.result_callback()
@click.pass_context
def result_callback(
    context: Context, result: Optional[Any], *args: Any, **kwargs: Any
) -> None:
    if isinstance(result, int):
        exit(result)


for command in COMMON_COMMANDS:
    cli.add_command(command)


if __name__ == "__main__":
    cli(default_map=default_map)
