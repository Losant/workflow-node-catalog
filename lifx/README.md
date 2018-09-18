# LIFX

Control [LIFX](https://www.lifx.com/) devices over the internet using the [LIFX HTTP API](https://api.developer.lifx.com/docs/).

## Input Configuration

* `LIFX App Token`: All requests to the LIFX API require an app token. You can generate an access token in your [account settings](https://cloud.lifx.com/settings). For more details, please refer to LIFX's [Authentication Documentation](https://api.developer.lifx.com/docs/authentication).
* `Action`: This node supports three API Actions: 
  * [List Lights](https://api.developer.lifx.com/docs/list-lights) - Filter the lights using [selectors](https://api.developer.lifx.com/docs/selectors).
  * [Set State](https://api.developer.lifx.com/docs/set-state) - Sets the state of the lights within the selector.
  * [Toggle](https://api.developer.lifx.com/docs/toggle-power) - Turn off lights if any of them are on, or turn them on if they are all off. 
* `Selector`: [Lifx selectors](https://api.developer.lifx.com/docs/selectors) are an identifier for addressing one or many lights belonging to the authenticated account.
* `Body`: The [Set State](https://api.developer.lifx.com/docs/set-state) and [Toggle](https://api.developer.lifx.com/docs/toggle-power) actions support the ability to include a body with the request. See their respective documentation to see what to include in the body.

## Output Result
The result of all successful requests will include a `body` property. The `body` object contains the response data.

```json
{
  "body":{
    "results": [
        {
            "id": "f043d559273c",
            "status": "ok",
            "label": "LIFX Light"
        }
    ]
  }
}
```

If the request to LIFX's API fails, the `body` property will contain an `error` object with additional details.

```json
{
  "body":{
    "error": "Token required"
  }
}
```

If the HTTP request fails, the `body` property will contain an `error` object with additional details.

```json
{
  "error":{
    "message": "Cannot resolve host: api.lifx.com",
  }
}
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 9/18/2018 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2018 Losant IoT, Inc

https://www.losant.com

