# GCP: Vision API

This node provides access to the [Google Vision API](https://cloud.google.com/vision/docs).

## Input Configuration

* `API Key`: The [Google Cloud API key](https://cloud.google.com/docs/authentication/api-keys).
* `Image Path`: The payload path to either a base64 encoded string or a URL to an existing image.
* `Image Type`: The type of image data that exists at the Image Path. Either a base64 encoded string or a URL.
* `Feature`: The Google Vision API [image annotate feature](https://cloud.google.com/vision/docs/reference/rest/v1/Feature) to use.
* `Max Results`: The maximum number of results to return.

## Output Result

The result of all successful requests will include `body`, `headers`, and `statusCode` fields. The `body` object contains the response data - an example is below.

```json
{
  "body": {
    "responses": [
      {
        "localizedObjectAnnotations": [
          {
            "boundingPoly": {
              "normalizedVertices": [
                {
                  "y": 0.2988766,
                  "x": 0.7113947
                },
                {
                  "y": 0.2988766,
                  "x": 0.86818737
                },
                {
                  "y": 0.3941245,
                  "x": 0.86818737
                },
                {
                  "y": 0.3941245,
                  "x": 0.7113947
                }
              ]
            },
            "score": 0.9073144,
            "name": "Car",
            "mid": "/m/0k4j"
          }
        ]
      }
    ]
  },
  "headers": { },
  "statusCode": 200
}
```

If the request is successfully made, but Google's Vision API returns an error, check the `statusCode` and `body` fields for additional details.

```json
{
  "body": {
    "error": {
      "status": "INVALID_ARGUMENT",
      "message": "API key not valid. Please pass a valid API key."
    }
  },
  "headers": { },
  "statusCode": 400
}
```

If the request to Google's Vision API fails, the output will contain an `error` object with additional details.

```json
{
  "error": {
    "message": "Cannot resolve host: vision.googleapis.com",
    "name": "ValidationError"
  }
}
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 4/30/2020 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2020 Losant IoT, Inc

<https://www.losant.com>
