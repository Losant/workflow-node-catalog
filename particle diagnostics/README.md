# Particle Diagnostics
This node provide access to [Particle's Remote Diagnostics API](https://docs.particle.io/reference/api/#remote-diagnostics) to retrieve device information.

## Input Configuration
* `Particle Access Key`: Your Particle API Access Key. You can obtain an API key through your Particle account settings.
* `Particle Device ID`: The Particle device ID to retrieve information about.
* `Method`: The API route you would like to call on the device.

## Output Result
The result of all successful requests will include `body`, `headers`, `statusCode` and `request` fields. The `body` object contains the response data.
The following is an example of the request body when calling the method 'Update'.

```json
{
  "body": {
    "ok": true
  }
}
```

If the request is successfully made, but Particles's API returns an error, check the `statusCode` and `body` fields for additional details.

```json
{
  "body": {
    "error_description":"The access token provided is invalid.",
    "error":"invalid_token"
  },
  "headers": { },
  "statusCode": 401
}
```

If the request to Particles's API fails, the output will contain an `error` object with additional details.

```json
{
  "error": {
    "message": "Cannot resolve host: api.particle.io",
  }
} 
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 8/6/2018 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright (c) 2018 Losant IoT, Inc

https://www.losant.com

