# Sigfox Get Device

This node provide access to Sigfox's REST API to retrieve a device's information.

## Input Configuration

* `Sigfox Username`: Your Sigfox API username.
* `Sigfox Password`: Your Sigfox API password.
* `Sigfox Device ID`: The Sigfox device ID to retrieve information about.

## Output Result

The result of all successful requests will include `body`, `headers`, and `statusCode` fields. The `body` object contains the response data.
The following is an example of the request body.

 ```json
{
  "body": {
    "automaticRenewal":true,
    "preventRenewal":false,
    "tokenEnd":0000,
    "contractId":"xxxx",
    "tokenType":"CONTRACT",
    "lng":0,
    "lat":0,
    "activationTime":1527116970285,
    "state":0,
    "averageRssi":-50.531433,
    "averageSnr":29.01479,
    "averageSignal":29.01479,
    "last":1533577884,
    "type":"xxxx",
    "name":"Device Name",
    "id":"Device ID"
  }
}
```

If the request is successfully made, but Sigfox's API returns an error, check the `statusCode` and `body` fields for additional details.

```json
{
  "body": {
    "message":"You are not allowed to access the resource."
  },
  "headers": {...},
  "statusCode": 403
}
```

If the request to Sigfox's API fails, the output will contain an `error` object with additional details.

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