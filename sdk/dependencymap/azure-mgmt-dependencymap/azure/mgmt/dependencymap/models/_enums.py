# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Extensible enum. Indicates the action type. "Internal" refers to actions that are for internal
    only APIs.
    """

    INTERNAL = "Internal"
    """Actions are for internal-only APIs."""


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of entity that created the resource."""

    USER = "User"
    """The entity was created by a user."""
    APPLICATION = "Application"
    """The entity was created by an application."""
    MANAGED_IDENTITY = "ManagedIdentity"
    """The entity was created by a managed identity."""
    KEY = "Key"
    """The entity was created by a key."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    """Indicates the operation is initiated by a user."""
    SYSTEM = "system"
    """Indicates the operation is initiated by a system."""
    USER_SYSTEM = "user,system"
    """Indicates the operation is initiated by a user or system."""


class ProcessNameFilterOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operator enum for process name filter."""

    CONTAINS = "contains"
    """Operator to include items in the result"""
    NOT_CONTAINS = "notContains"
    """Operator to exclude items in the result"""


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the resource."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    PROVISIONING = "Provisioning"
    """This state indicates that the resource is being provisioned."""
    UPDATING = "Updating"
    """This state indicates that the resource is being updated."""
    DELETING = "Deleting"
    """This state indicates that the resource is being deleted."""
    ACCEPTED = "Accepted"
    """This state indicates that the operation on the resource has been accepted."""


class SourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Source type of the discoverySource."""

    OFF_AZURE = "OffAzure"
    """OffAzure source type"""
