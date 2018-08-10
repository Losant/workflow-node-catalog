# Loggly
Log payload data to Loggly using their [HTTP API](https://www.loggly.com/docs/http-endpoint/).

## Input Configuration
* `Loggly Customer Token`: [Customer Tokens](http://loggly.com/docs/customer-token-authentication-token/) are used by Loggly to associate data you send with your account. The token is used as part of the API request.
* `Event Data`: The payload path of event data to send to Loggly..

## Output Result
The result of all successful requests will include `body`, `headers`, and `statusCode` fields. The `body` object contains the response data.

```json
{"response" : "ok"}
```

If the request is successfully made, but Loggly's API returns an error, check the `statusCode` and `body` fields for additional details.

```json
{
  "body": "Invalid API key",
  "headers": { },
  "statusCode": 403
}
```

If the request to Loggly's API fails, the output will contain an `error` object with additional details.

```json
{
  "error": {
    "message": "Cannot resolve host: logs-01.loggly.com",
  }
} 
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 8/10/2018 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2018 Losant IoT, Inc

https://www.losant.com

