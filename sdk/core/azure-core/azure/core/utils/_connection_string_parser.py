# coding=utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Mapping


def parse_connection_string(conn_str: str, case_sensitive_keys: bool = False) -> Mapping[str, str]:
    """Parses the connection string into a dict of its component parts, with the option of preserving case
    of keys, and validates that each key in the connection string has a provided value. If case of keys
    is not preserved (ie. `case_sensitive_keys=False`), then a dict with LOWERCASE KEYS will be returned.

    :param str conn_str: String with connection details provided by Azure services.
    :param bool case_sensitive_keys: Indicates whether the casing of the keys will be preserved. When `False`(the
        default), all keys will be lower-cased. If set to `True`, the original casing of the keys will be preserved.
    :rtype: Mapping
    :returns: Dict of connection string key/value pairs.
    :raises ValueError: if each key in conn_str does not have a corresponding value and
            for other bad formatting of connection strings - including duplicate
            args, bad syntax, etc.
    """

    cs_args = [s.split("=", 1) for s in conn_str.strip().rstrip(";").split(";")]
    if any(len(tup) != 2 or not all(tup) for tup in cs_args):
        raise ValueError("Connection string is either blank or malformed.")
    args_dict = dict(cs_args)

    if len(cs_args) != len(args_dict):
        raise ValueError("Connection string is either blank or malformed.")

    if not case_sensitive_keys:
        # if duplicate case insensitive keys are passed in, raise error
        new_args_dict = {}
        for key in args_dict.keys():  # pylint: disable=consider-using-dict-items
            new_key = key.lower()
            if new_key in new_args_dict:
                raise ValueError("Duplicate key in connection string: {}".format(new_key))
            new_args_dict[new_key] = args_dict[key]
        return new_args_dict

    return args_dict
