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

from flask import Blueprint, render_template
from invenio_rdm_records.resources.serializers import UIJSONSerializer
from opensearch_dsl.utils import AttrDict

from .search import FrontpageRecordsSearch

blueprint = Blueprint(
    "invenio-override",
    __name__,
    template_folder="templates",
    static_folder="static",
)


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

    # blueprint.add_url_rule(routes["index"], view_func=index)
    blueprint.add_url_rule(routes["comingsoon"], view_func=comingsoon)

    return blueprint


def records_serializer(records=None):
    """Serialize list of records."""
    record_list = []
    for record in records:
        record_list.append(UIJSONSerializer().dump_obj(record.to_dict()))
    return record_list


def index():
    """Frontpage."""
    records = FrontpageRecordsSearch()[:5].sort("-created").execute()

    return render_template(
        "invenio_override/index.html", records=records_serializer(records)
    )


def comingsoon():
    """Comingsoon."""
    return render_template("invenio_override/comingsoon.html")


def locked(e):
    """Error page for status locked."""
    return render_template("invenio_override/423.html")


def generate_search_url(query="", layout="list", page=1, size=10, sort="newest"):
    """Generate a general search URL with sensible defaults."""
    return url_for(
        "invenio_search_ui.search",
        q=query,
        l=layout,
        page=page,
        size=size,
        sort=sort,
    )


@blueprint.app_context_processor
def inject_search_url():
    """Inject the search URL generator into the template context."""
    return dict(generate_search_url=generate_search_url)
