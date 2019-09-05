# -*- coding: utf-8 -*-
# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from argparse import RawDescriptionHelpFormatter

from conda.cli import common
from conda.cli.conda_argparse import add_parser_prefix, add_parser_json
from conda.core.envs_manager import list_all_known_prefixes

description = """
Interact with environment varaibles associated with Conda environments
"""

example = """
examples:
    conda env vars --list -n my_env
    conda env vars --set MY_VAR=something
    conda env vars --unset MY_VAR 
"""


def configure_parser(sub_parsers):
    p = sub_parsers.add_parser(
        'vars',
        formatter_class=RawDescriptionHelpFormatter,
        description=description,
        help=description,
        epilog=example,
    )

    p.add_argument(
        '-l', '--list',
        action='store',
        help='list environment variables',
        default=False,
    )

    p.add_argument(
        '-s', '--set',
        action='store',
        help='set environment variables',
        default=None,
    )

    p.add_argument(
        '-u', '--unset',
        action='store',
        help='unset environment variables',
        default=None,
    )

    # Add name and prefix args
    add_parser_prefix(p)
    add_parser_json(p)
    p.set_defaults(func='.main_vars.execute')


def execute(args, parser):


    if args.json:
        common.stdout_json("")
