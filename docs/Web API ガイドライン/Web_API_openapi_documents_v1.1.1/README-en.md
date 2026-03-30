## ECHONET Lite Web API : OpenAPI documentations

### 1. About this archive

This archive has been created to provide OpenAPI documents that correspond to the various descriptions defined in the ECHONET Lite Web API Guidelines.
OpenAPI documents are REST API definition specifications promoted by the [OAI (OpenAPI Initiative)](https://www.openapis.org) (see [OAS (OpenAPI Specification)](https://spec.openapis.org/oas/latest.html)).  
Various tools have been developed using the OpenAPI documents to enable API server stub code (skeleton) generation, supported client code generation, mock server generation, automated API testing and specification viewer, and the ecosystem is rich with features such as tool examples.  

Examples of tools:
- Stoplight Studio (editor), Prism (mock), Dredd (testing), openapi-generator (code generation), redoc (specification viewer).

### 2. Positioning and limitations of this tool

The OpenAPI documents in this archive are based on the ECHONET Lite Web API Guidelines and are converted from various descriptions, such as Device Descriptions defined for each device and Bulk Descriptions provided as Application APIs, based on certain rules.  Descriptions can basically be obtained by calling the GET method on ``/elapi/v1/<service type>/<ID>`''.  

Each OpenAPI document uses only the information in the various descriptions as conversion source information, so only the content specified in the properties (GET and PUT methods) and actions (POST method) in the descriptions is subject to conversion.  
The guidelines do not support the PATCH and DELETE methods, although some APIs do. Please note that these APIs will need to be added or modified as required.  
In addition, the OpenAPI document is normally prepared as a single file, but this archive provides the document into separate files for each target service type and resource. If you want to use individual APIs in isolation, you can use them as they are, but if necesssary, you should select multiple OpenAPI documents for the server you are developing and merge them into a single file.

Details of other limitations are described below.

### 3. Supported guideline versions

This archive supports the API Specification section V.1.1.7 and the Device Specification section V.1.6.0 of the ECHONET Lite Web API Guidelines.  
The application service function of the API specification section supports the bulk/group/history/resHistory descriptions.  
The device specification section supports all released devices (device description). Note that the OpenAPI document corresponding to the ECHONET Lite device superclass is output as a separate file (openapi_commonItems.yaml), so the content of this device superclass must be added to the OpenAPI document for each device.

### 4. file and folder structure

```
./ 
│  README.md
│  README-en.md
│  LICENSE
│  openapi_elapi_v1_desivces.yaml # prepared OpenAPI documentation for base path
│
├─dd # Collection of Device Descriptions of the conversion source
│      airCleaner.json
│      ...
│
├─ext-apis # Collection of Descriptions for the application API of the conversion source
│      bulks.json
│      groups.json
│      histories.json
│      ...
│
└─out # OpenAPI documents (Converted from Device Descriptions and application API Descriptions)
        openapi_airCleaner.yaml
        ...
```

### 5. other, limitations, etc.

**Specify version, server information, etc**.

The version of `openapi` is 3.0.3; the latest version of OAS is 3.1.0, but considering the fact that there are few tools that support it at the moment, the 3.0 series is used. 

Dummy data is included for `info` and `servers`. Please change these according to the developer's server environment.

**Merge any OpenAPI document**.

As mentioned above, it is necessary to merge several OpenAPI documents when actually building a server. In the case of building a server with ECHONET Lite Web API for a single device, the following documents need to be merged

- OpenAPI document for the base path: openapi_elapi_v1_devices.yaml
- OpenAPI document for the superclass: openapi_commonItems.yaml
- OpenAPI document for a device: openapi_xx.yaml (where xx is the device type name)

If you want to support other devices, please add an OpenAPI document for the target device.

If using application APIs such as bulks, openapi_bulks.yaml etc. should be added in time.

When merging the content of items in each document, the `openapi`,`servers`, `info` and `security` items should be added in an array,
`tags` should be added in an array, and `paths` and `components` should be listed together, taking care to avoid duplicate entries (see below).

**Notes on merging OpenAPI documents**.

Although the URIs for different devices (models) are different in the ECHONET Lite Web API, in some cases they are expressed as the same path in the OpenAPI definition. For example, if a batch property acquisition is attempted for a device (storage battery) with a device ID of `0001` and a device (PV) with a device ID of `0002`, the ECHONET Lite Web API uses `/elapi/v1/devices/0001/properties` and `/elapi/`. In OpenAPI, `0001` and `0002` are represented by path parameters, so in the `paths` the GET method is called for the endpoint `/elapi/v1/devices/0002/properties` in any case. `devices/{device_id}/{device_id}/properties`. The API to call is the same, but the response body is different for devices X and Y. If merging is required, the contents of X and Y are combined with `oneOf` in `schema` in the success code of the `responses`.

```yaml
              schema:
                oneOf:
                -  $ref: '#/components/schemas/propertiesStorageBattery'
                -  $ref: '#/components/schemas/propertiesPvPowerGeneration'
```

The above shows an example for `properties`, but note that the same merging process is required for each property resource under `properties`, as the same name may be used for each property resource, even though the devices are different.

If the same property resource name is also handled in the PUT method, etc., it is necessary to use `oneOf` in the same way if the request body is different for each of them.

When merging OpenAPI documents for multiple devices (models), it is necessary to list each tag in the `tags` content where the paths are the same.

In addition, there may be cases of duplicate entries in the `components` section, so please edit the section in time to avoid problems with duplicate entries.


**required specification**.

The `required` specification for each key in `properties` has not been implemented.
Please add them if necessary.


**Example values

Example values are not described.
Please add if necessary.

**Response Status Code***.

Status codes in the response are only 200, 401 for all APIs.
If you need to change 200 to 201 or 400 or 500 series error codes, please change or add them in time.

**Security**.

For example, only API keys are supported.
If you wish to use other methods (e.g. ID tokens), please modify in good time.

In the example output, "`X-Elapi-key`" is used as the key name for the API key. If you want to use a different key name, change it accordingly.

### 7. Conversion rules

The following rules are generally applied when converting different descriptions into OpenAPI documents.


- `tags`: use class names
- `summary`: HTTP method + property resource name
- `operationId`: HTTP method + one of `devices`/`bulks`/`groups`/`histories`/`resHistories` + property resource name + class name
- `description`: for GET method, get + resource name property; for PUT method, set + resource name property; for POST method, execute + resource name property
- `parameters`, `requestBody`, `responses`: generated from the corresponding schema of the different descriptions. However, the following points should be noted:
  - In the `schema`, `unit`, `values`, `descriptions` and `coefficient` used in the schema in the different Descriptions are not available and should be deleted during the conversion.

### 8. License.

Distributed under the MIT license. See LICENSE for more information.


