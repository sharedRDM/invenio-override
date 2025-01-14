# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2023 Graz University of Technology.
# Copyright (C) 2024 Shared RDM.
#
# invenio-override is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for sharedRDM theme."""

from typing import Dict

from flask import Blueprint, current_app, render_template
from invenio_rdm_records.resources.serializers import UIJSONSerializer
from invenio_records_global_search.resources.serializers import (
    GlobalSearchJSONSerializer,
)
from opensearch_dsl.utils import AttrDict

from .search import FrontpageRecordsSearch

blueprint = Blueprint(
    "invenio_override",
    __name__,
    template_folder="templates",
    static_folder="static",
)


def records_serializer(records=None):
    """Serialize list of records."""
    serializer = GlobalSearchJSONSerializer()
    return [serializer.dump_obj(r.to_dict()) for r in records]


def index():
    """Frontpage."""
    records = FrontpageRecordsSearch()[:5].sort("-created").execute()

    return render_template(
        "invenio_override/frontpage.html", records=records_serializer(records)
    )


def default_error_handler(e: Exception):
    """Called when an otherwise unhandled error occurs."""
    # TODO: use sentry here once it's configured
    # information we might want to log for debugging the error:
    #   - `flask.request`, a proxy to the current http-request in which the error occured
    #   - `flask.session`, a proxy to the current http-session
    #   - `e`, the passed-in exception
    # to get proxied-to objects: `flask.request._get_current_object()`

    return render_template(current_app.config["THEME_500_TEMPLATE"]), 500


@blueprint.app_template_filter("make_dict_like")
def make_dict_like(value: str, key: str) -> Dict[str, str]:
    """Convert the value to a dict like structure.

    in the form of a key -> value pair.
    """
    return {key: value}


@blueprint.app_template_filter("cast_to_dict")
def cast_to_dict(attr_dict):
    """Return the dict structure of AttrDict variable."""
    return AttrDict.to_dict(attr_dict)


def ui_blueprint(app):
    """Blueprint for the routes and resources provided by Invenio-theme-tugraz."""
    routes = app.config.get("OVERRIDE_ROUTES")

    blueprint.add_url_rule(routes["index"], view_func=index)
    # blueprint.add_url_rule(routes["comingsoon"], view_func=comingsoon)
    return blueprint


@blueprint.app_template_filter("make_dict_like")
def make_dict_like(value: str, key: str) -> Dict[str, str]:
    """Convert the value to a dict like structure.

    in the form of a key -> value pair.
    """
    return {key: value}


def comingsoon():
    """Comingsoon."""
    return render_template("invenio_override/comingsoon.html")


def locked(e):
    """Error page for status locked."""
    return render_template("invenio_override/423.html")
