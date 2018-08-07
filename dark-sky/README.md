# Dark Sky
This node provide access to [Dark Sky's Forecast API](https://darksky.net/dev/docs#forecast-request).

## Input Configuration
* `Dark Sky API Key`: Your Dark Sky API key.
* `GPS Coordinates`: The GPS Coordinates to retrieve weather for in decimal degrees format (e.g. 39.108,-84.509).

## Output Result
The result of all successful requests will include `body`, `headers`, and `statusCode` fields. The `body` object contains the response data.

```json
{
  "body": {
    "offset": -4,
    "flags": { },
    "daily": { },
    "hourly": { },
    "minutely": { },
    "currently": {
      "ozone": 298.35,
      "visibility": 9.07,
      "uvIndex": 3,
      "cloudCover": 0.7,
      "windBearing": 245,
      "windGust": 5.32,
      "windSpeed": 3.78,
      "pressure": 1019.06,
      "humidity": 0.49,
      "dewPoint": 68.76,
      "apparentTemperature": 95.1,
      "temperature": 90.47,
      "precipProbability": 0,
      "precipIntensity": 0,
      "nearestStormBearing": 167,
      "nearestStormDistance": 2,
      "icon": "partly-cloudy-day",
      "summary": "Mostly Cloudy",
      "time": 1533413754
    },
    "timezone": "America/New_York",
    "longitude": -84.509,
    "latitude": 39.108
  },
  "headers": { },
  "statusCode": 200
}
```

If the request is successfully made, but Dark Sky's API returns an error, check the `statusCode` and `body` fields for additional details.

```json
{
  "body": "Forbidden\n",
  "headers": { },
  "statusCode": 403
}
```

If the request to Dark Sky's API fails, the output will contain an `error` object with additional details.

```json
{
  "error": {
    "message": "Cannot resolve host: api.darksky.net",
  }
} 
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 8/4/2018 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2018 Losant IoT, Inc

https://www.losant.com

