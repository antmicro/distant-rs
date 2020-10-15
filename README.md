# distant-rs

Copyright (c) 2019-2020 [Antmicro](https://www.antmicro.com)

This repository contains code of `distant-rs`, a library for uploading and processing invocations in services implementing [Google's ResultStore API](https://github.com/googleapis/googleapis/tree/master/google/devtools/resultstore/v2).

## Installation

In order to install the library, clone this repository and run `pip3 install distant-rs/`.

## Configuration

If an application implementing this library is running inside the Compute Engine, all requests will be authenticated using [Application Default Credentials](https://cloud.google.com/docs/authentication/production) and the project ID will be pulled from the [GCE's Metadata Server](https://cloud.google.com/compute/docs/storing-retrieving-metadata).

However, if that's not the case, the `GOOGLE_APPLICATION_CREDENTIALS` and `GOOGLE_PROJECT_ID` environment variables must be set to the path of a file containing JSON-encoded service account credentials and to the [project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) respectively.

Additionally, make sure that the `DISTANT_RS_BUCKET` environment is set to the name of a Google Cloud Storage bucket where log files and artifacts will be uploaded.
The aforementioned service account must have the write access to the bucket, as well as the bucket must [publicly accessible](https://cloud.google.com/storage/docs/access-control/making-data-public) (i.e. the `allUsers` role has the `Storage Object Viewer` permission).

All of the parameters specified above override the values provided in the constructor of the `Invocation` class.

## License

[Apache 2.0](LICENSE)
