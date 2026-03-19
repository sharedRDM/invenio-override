// Copyright (C) 2025 Shared RDM.
// invenio-override is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.
//
// This bundle must be loaded BEFORE invenio-app-rdm-user-uploads.js so that
// overrideStore.getAll() in uploads.js picks up these overrides.

import { overrideStore } from "react-overridable";
import { UploadsResults } from "./UploadsResults";

const appName = "InvenioAppRdm.DashboardUploads";

overrideStore.add(`${appName}.SearchApp.results`, UploadsResults);
