# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology.
#
# invenio-override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Permission generators that can be configured from the instance."""

from flask import current_app
from flask_principal import RoleNeed
from invenio_records_permissions.generators import Generator


class CommunityCreator(Generator):
    """Grant permissions to users with configured community-creator roles.

    Roles are configured via the `OVERRIDE_COMMUNITIES_CREATE_ROLES` config variable.
    """

    def needs(self, record=None, **kwargs):
        roles = current_app.config.get(
            "OVERRIDE_COMMUNITIES_CREATE_ROLES", ["community-creator"]
        )
        return [RoleNeed(r) for r in roles]
