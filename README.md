<!--
  Copyright (C) 2020-2026 Graz University of Technology.

  invenio-override is free software; you can redistribute it and/or
  modify it under the terms of the MIT License; see LICENSE file for more
  details.
-->

# invenio-override

[![CI](https://github.com/tu-graz-library/invenio-override/workflows/CI/badge.svg)](https://github.com/tu-graz-library/invenio-override/actions)
[![PyPI downloads](https://img.shields.io/pypi/dm/invenio-override.svg)](https://pypi.python.org/pypi/invenio-override)
[![Release](https://img.shields.io/github/tag/tu-graz-library/invenio-override.svg)](https://github.com/tu-graz-library/invenio-override/releases)
[![License](https://img.shields.io/github/license/tu-graz-library/invenio-override.svg)](https://github.com/tu-graz-library/invenio-override/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An InvenioRDM package based on [InvenioRDM](https://inveniosoftware.org/products/rdm/), built and maintained by [Graz University of Technology](https://www.tugraz.at).

`invenio-override` is installed as a package in your InvenioRDM instance. Each institution provides their own theme on top of it. Same package, different institutions.

---

## How it works

In your InvenioRDM instance, create a theme folder (e.g. `themes/TUG/`) with:
- `variables.less` — institution colors and typography
- `overrides.less` — component-level tweaks
- `invenio.cfg` — branding, enabled features, footer links

At build time the LESS files are applied on top of the base theme. Everything else is configured at runtime via `invenio.cfg`.

See [`invenio.cfg.example`](invenio.cfg.example) for all available `OVERRIDE_*` variables.

---

## Supports

- [invenio-global-search](https://github.com/tu-graz-library/invenio-global-search)
- [invenio-curations](https://github.com/tu-graz-library/invenio-curations)
- [invenio-records-lom](https://github.com/tu-graz-library/invenio-records-lom) (OER)
- [invenio-records-marc21](https://github.com/tu-graz-library/invenio-records-marc21) (Publications)

