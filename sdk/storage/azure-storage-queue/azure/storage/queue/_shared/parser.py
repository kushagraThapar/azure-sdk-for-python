# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from datetime import datetime, timezone
from typing import Optional

EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS filetime
HUNDREDS_OF_NANOSECONDS = 10000000


def _to_utc_datetime(value: datetime) -> str:
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def _rfc_1123_to_datetime(rfc_1123: str) -> Optional[datetime]:
    """Converts an RFC 1123 date string to a UTC datetime.

    :param str rfc_1123: The time and date in RFC 1123 format.
    :return: The time and date in UTC datetime format.
    :rtype: datetime
    """
    if not rfc_1123:
        return None

    return datetime.strptime(rfc_1123, "%a, %d %b %Y %H:%M:%S %Z")


def _filetime_to_datetime(filetime: str) -> Optional[datetime]:
    """Converts an MS filetime string to a UTC datetime. "0" indicates None.
    If parsing MS Filetime fails, tries RFC 1123 as backup.

    :param str filetime: The time and date in MS filetime format.
    :return: The time and date in UTC datetime format.
    :rtype: datetime
    """
    if not filetime:
        return None

    # Try to convert to MS Filetime
    try:
        temp_filetime = int(filetime)
        if temp_filetime == 0:
            return None

        return datetime.fromtimestamp((temp_filetime - EPOCH_AS_FILETIME) / HUNDREDS_OF_NANOSECONDS, tz=timezone.utc)
    except ValueError:
        pass

    # Try RFC 1123 as backup
    return _rfc_1123_to_datetime(filetime)
