# Algolia - Search Index with HTTPS GET

This node provides access to [Algolia's Search Index HTTPS GET API](https://www.algolia.com/doc/rest-api/search/#search-index-get).

## Input Configuration

* `Algolia Application ID`: The Algolia Application ID.
* `Algolia Application Key`: The Algolia Application Key.
* `Algolia Index Name to Search`: The Algolia Index Name to search.
* `Search Parameters`: The Algolia [Search Parameters](https://www.algolia.com/doc/api-reference/search-api-parameters/) that can be used with your search criteria to search your index.

## Output Result

The result of all successful requests will include `body`, `headers`, and `statusCode` fields. The `body` object contains the response data - an example is below.

```json
{
  "body": {
    "exhaustiveNbHits": true,
    "hits": [
      {
        "_highlightResult": {
          "code": {
            "matchedWords": [
            ],
            "matchLevel": "none",
            "value": "16"
          },
          "type": {
            "matchedWords": [
            ],
            "matchLevel": "none",
            "value": "1"
          }
        },
        "cause": "I/O communication configuration fault detected. (CompactLogix 1768-L4x controllers only.)",
        "code": "16",
        "objectID": "734455050",
        "recoveryMethod": "Reconfigure the number of communication modules on the 1768 bus side of the controller: 1. 1768-L43 has a maximum of two modules. 2. 1768-L45 has a maximum of four modules. 2a. Up to four Sercos modules 2b. Up to two NetLinx communication modules",
        "type": "1"
      }
    ],
    "hitsPerPage": 20,
    "nbHits": 1,
    "nbPages": 1,
    "page": 0,
    "params": "facetFilters=[[%22code:16%22],[%22type:1%22]]",
    "processingTimeMS": 1,
    "query": ""
  },
  "headers": { },
  "statusCode": 200
}
```

If the request is successfully made, but Algolia's API returns an error, check the `statusCode` and `body` fields for additional details.

```json
{
  "body": {
    "message": "Invalid Application-ID or API key",
    "status": 403
  },
  "headers": { },
  "statusCode": 403
}
```

If the request to Dark Sky's API fails, the output will contain an `error` object with additional details.

```json
{
  "error": {
    "message": "Cannot resolve host: my-application-id-dsn.algolia.net",
    "name": "ValidationError"
  }
}
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 3/11/2019 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2019 Losant IoT, Inc

<https://www.losant.com>
