# Redact Payload

Redacts a payload, obscuring sensitive values based on property names.

_Note: Property values are not searched, only property names._

## Input Configuration

- `Payload Path`: The payload path containing the object to recursively search and redact.
- `Additional Strings to Redact`: Optional additional string(s) denote sensitive keys.

## Output Result

The output will be a recursively redacted copy of the payload found at `path`. Any property names containing one of a list of keywords will have its value replaced with `*****REDACTED*****`. This redaction protects sensitive data when saving or sending a payload.

For instance, when using the `Workflow Error` trigger node, you may wish to to email yourself a copy of any errored payloads, but _not_ wish to have sensitive data included in the email.

The default list of keywords denoting values to be redacted is `secret`, `token`, `password`, `auth`, and `key`. Additional keywords can be specified using the `keysToRedactCSV` input. For instance, a value for this input of `hello,sensitive` will add both `hello` and `sensitive` to the default list of keywords.

## Example:

Given a `keysToRedactCSV` value of `hello,sensitive`, and the payload:

```
{
  "clean":"sparkling",
  "someSecretishThing":"The key is 42.",
  "additionalSensitiveData":"password123",
  "aNestedObject":{
      "token": "abc123"
  },
  "values":[
    {
      "password":"alphabravocharlie"
    }
  ]
}
```

the returned value will be:

```
{
  "clean": "sparkling",
  "someSecretishThing": "*****REDACTED*****",
  "additionalSensitiveData":"*******REDACTED*******",
  "aNestedObject": {
    "token": "*****REDACTED*****"
  },
  "values": [
    {
      "password": "*****REDACTED*****"
    }
  ]
}
```

## Version History

| Version | Date      | Description      |
| ------- | --------- | ---------------- |
| v1.0.0  | 7/18/2020 | Initial release. |

---

This node was developed by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2020 Losant IoT, Inc

<https://www.losant.com>
