# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology.
#
# invenio-override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Permission policies that can be configured from the instance."""

from invenio_administration.generators import Administration
from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_records_permissions.generators import (
    AuthenticatedUser,
    IfConfig,
    SystemProcess,
)

from invenio_override.generators import CommunityCreator


class CustomCommunitiesPermissionPolicy(CommunityPermissionPolicy):
    """Custom permission policy for communities."""

    can_create = [
        IfConfig(
            "OVERRIDE_COMMUNITIES_RESTRICT_CREATION",
            then_=[CommunityCreator(), Administration(), SystemProcess()],
            else_=[AuthenticatedUser(), SystemProcess()],
        )
    ]

    can_include_directly = [Administration(), SystemProcess()]
