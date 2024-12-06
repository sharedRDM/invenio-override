# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2023 Graz University of Technology.
# Copyright (C) 2024 Shared RDM.
#
# invenio-override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for sharedRDM theme."""

from . import config
from .views import locked


class InvenioOverride(object):
    """Invenio override extension."""

    def __init__(self, app=None):
        """Initialize the extension."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the Flask app."""
        self.init_config(app)
        app.register_error_handler(423, locked)

        @app.context_processor
        def inject_security_settings():
            return {
                "security": {
                    key: app.config.get(key, False)
                    for key in app.config
                    if key.startswith("SECURITY_")
                }
            }

        app.extensions["invenio-override"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("INVENIO_OVERRIDE_") or k.startswith("OVERRIDE_"):
                app.config.setdefault(k, getattr(config, k))

        app.config.setdefault("SECURITY_REGISTERABLE", False)
        app.logger.debug(
            f"SECURITY_REGISTERABLE set to: {app.config['SECURITY_REGISTERABLE']}"
        )
        self.check_configuration_consistency(app)

    def check_configuration_consistency(self, app):
        """Verify configuration consistency."""
        sec = app.extensions.get("security")
        if sec:
            local_login = app.config.get("ACCOUNTS_LOCAL_LOGIN_ENABLED", False)
            local_account_editable = (
                sec.registerable or sec.changeable or sec.recoverable
            )
            if local_account_editable and not local_login:
                app.logger.warning(
                    "ACCOUNTS_LOCAL_LOGIN_ENABLED is False, but at least one of "
                    "SECURITY_REGISTERABLE, SECURITY_RECOVERABLE, or SECURITY_CHANGEABLE "
                    "is True. This may cause inconsistencies."
                )
