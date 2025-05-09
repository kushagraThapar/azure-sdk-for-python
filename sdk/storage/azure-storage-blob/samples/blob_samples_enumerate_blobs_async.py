# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: blob_samples_enumerate_blobs_async.py
DESCRIPTION:
    This sample demos how to enumerate a container and print all blobs.
USAGE: python blob_samples_enumerate_blobs_async.py
    Set the environment variables with your own values before running the sample:
    1) STORAGE_CONNECTION_STRING - the connection string to your storage account
"""

import os
import sys
import asyncio
from azure.storage.blob.aio import ContainerClient

async def main():
    try:
        CONNECTION_STRING = os.environ['STORAGE_CONNECTION_STRING']
    except KeyError:
        print("STORAGE_CONNECTION_STRING must be set.")
        sys.exit(1)

    container = ContainerClient.from_connection_string(CONNECTION_STRING, container_name="mycontainerenumerateasync")
    await container.create_container()
    async with container:
        async for blob in container.list_blobs():
            print(blob.name + '\n')

if __name__ == "__main__":
    asyncio.run(main())
