# GCP: OAuth

This node generates [OAuth Tokens](https://developers.google.com/identity/protocols/OAuth2ServiceAccount) from [Google Cloud Service Accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts). These tokens can then be used to make service-to-service requests against any number of [Google APIs](https://developers.google.com/apis-explorer/#p/) using the [HTTP Node](https://docs.losant.com/workflows/data/http/). This is primarily intended to make API requests to Google Cloud services, like [IoT Core](https://cloud.google.com/iot/docs/reference/rest/).

Tokens are automatically cached and re-fetched when they expire.

## Input Configuration

* `Service Account Key`: A Google Cloud [Service Account Key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys), in JSON format.
* `Scope`: The [OAuth Scope](https://developers.google.com/identity/protocols/googlescopes) to request a token for. The Service Account must have the appropriate privileges to request the supplied scope.

## Output Result

If the result is successful, the result will contain a single `token` field with the OAuth token.

```json
{
  "token": "your-oauth-token"
}
```


If the request fails, the output will contain an `error` object with additional details.

```json
{
  "error": {
    "error_description": "https://www.googleapis.com/auth/bad-scope is not a valid audience string.",
    "error": "invalid_scope"
  }
}
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 7/16/2019 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2019 Losant IoT, Inc

<https://www.losant.com>
