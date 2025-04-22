# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2023 Graz University of Technology.
# Copyright (C) 2024 Shared RDM.
#
# invenio-override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""LOM override for invenio-override."""

import invenio_records_lom.ext
from invenio_records_lom.ext import InvenioRecordsLOM


class InvenioOverrideLOM(InvenioRecordsLOM):
    """Override LOM extension."""

    def __init__(self, app=None):
        """Initialize extension."""
        if app and app.config.get("OVERRIDE_SHOW_EDUCATIONAL_RESOURCES", False):
            super().__init__(app)


# Replace the original LOM extension with our version
invenio_records_lom.ext.InvenioRecordsLOM = InvenioOverrideLOM
