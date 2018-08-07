# Address Lookup
This node will do a GPS location reverse lookup and return the associated address with a location. The lookup is done using [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro#ReverseGeocoding). In order you will need an API key from [Google Cloud Platform](https://developers.google.com/maps/documentation/geocoding/get-api-key). 

## Input Configuration
* `Google Maps API Key`: Your Google Cloud Maps API key.
* `GPS Coordinates`: The GPS Coordinates to look up the address for in decimal degrees format (e.g. 39.108,-84.509).

## Output Result
The result of all successful requests will include `address`, `body`, `headers`, and `statusCode` fields. The `address` field will have the full address returned.

```json
{
  "address": "1100 Sycamore St. Cincinnati, OH 45202",
  "body": { },
  "headers": { },
  "statusCode": 200
}
```

The `body` object contains the entire response data from the API. This can be used to get more granular data.

```json
{
  "address": "3324 NJ-37, Toms River, NJ 08753, USA",
  "body": {
  	"status": "OK",
    "results": [
      {
        "types": ["premise"],
        "place_id": "ChIJNa4V0vCbwYkRZpTYaESqt6Y",
        "geometry": { },
        "formatted_address": "3324 NJ-37, Toms River, NJ 08753, USA",
        "address_components": [
          {
            "types": [
              "street_number"
            ],
            "short_name": "3324",
            "long_name": "3324"
          },
          {
            "types": [
              "route"
            ],
            "short_name": "NJ-37",
            "long_name": "New Jersey 37"
          },
          {
            "types": [
              "locality",
              "political"
            ],
            "short_name": "Toms River",
            "long_name": "Toms River"
          },
          {
            "types": [
              "administrative_area_level_2",
              "political"
            ],
            "short_name": "Ocean County",
            "long_name": "Ocean County"
          },
          {
            "types": [
              "administrative_area_level_1",
              "political"
            ],
            "short_name": "NJ",
            "long_name": "New Jersey"
          },
          {
            "types": [
              "country",
              "political"
            ],
            "short_name": "US",
            "long_name": "United States"
          },
          {
            "types": [
              "postal_code"
            ],
            "short_name": "08753",
            "long_name": "08753"
          },
          {
            "types": [
              "postal_code_suffix"
            ],
            "short_name": "6293",
            "long_name": "6293"
          }
        ]
      },
      { },
      { },
      { },
      { },
      { },
      { },
      { },
      { }
    ]
  },
  "headers": { },
  "statusCode": 200
}
```

If the request is successfully made, but the API returns an error, check the `statusCode` and `body` fields for additional details.

```json
{
  "body": {
  	"status": "REQUEST_DENIED",
  	"results": [],
  	"error_message": "The provided API key is invalid."
  },
  "headers": { },
  "statusCode": 403
}
```

If the request to Google Maps API fails, the output will contain an `error` object with additional details.

```json
{
  "error": {
    "message": "Cannot resolve host: maps.googleapis.com",
  }
} 
```

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 8/6/2018 | Initial release. |

---

This node is developed and maintained by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2018 Losant IoT, Inc

https://www.losant.com