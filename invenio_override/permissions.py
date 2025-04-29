# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Shared RDM.
#
# invenio-override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Custom permissions for the Invenio Override module."""

from invenio_records_marc21.services.permissions import Marc21RecordPermissionPolicy
from invenio_records_permissions.generators import (
    AnyUser,
    AuthenticatedUser,
    SystemProcess,
)


class LenientMarc21PermissionPolicy(Marc21RecordPermissionPolicy):
    """A more lenient policy allowing read access to restricted metadata and files for authenticated users."""

    # Allow anyone (including anonymous users) to read the metadata of any record,
    # even if the record itself is restricted. File access is handled separately.
    can_read = [AnyUser(), SystemProcess()]

    # Allow authenticated users to read restricted files
    can_read_files = [AuthenticatedUser(), SystemProcess()]

    # Keep other permissions potentially strict (like the default)
    # For example, file access might still require specific permissions
    can_create = Marc21RecordPermissionPolicy.can_create
    can_update = Marc21RecordPermissionPolicy.can_update
    can_delete = Marc21RecordPermissionPolicy.can_delete
    # Add other 'can_*' attributes as needed, inheriting from the base policy

    # If you need draft permissions:
    # can_edit = Marc21RecordPermissionPolicy.can_edit
    # can_new_version = Marc21RecordPermissionPolicy.can_new_version
    # can_manage = Marc21RecordPermissionPolicy.can_manage
    # can_update_draft = Marc21RecordPermissionPolicy.can_update_draft
    # can_read_draft = Marc21RecordPermissionPolicy.can_read_draft
    # can_delete_draft = Marc21RecordPermissionPolicy.can_delete_draft
