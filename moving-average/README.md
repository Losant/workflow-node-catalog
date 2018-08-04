# Moving Average
Calculates a moving average over a configurable number of data points.

## Input Configuration
* `Count`: The number of values to average together.
* `Average Identifier`: Optional identifier that allows this node to perform moving averages for multiple sets of data.
* `Value`: The value to average.

## Output Result
The output will be `null` until at least `Count` data points have been received. Once enough data points have been received, the output will be the calculated moving average. The `Average Identifier` property allows this node to calculate multiple sets of moving averages based on this identifier. For example, if you wanted to calculate a moving average for an attribute of many different devices, the identifier could be set to the device ID.

The moving average is stored in workflow storage for a specific instance of this node. Deleting this node from the canvas and re-adding a new one will reset the moving average calculation.

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 8/4/2018 | Initial release. |

---

This node was developed by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright (c) 2018 Losant IoT, Inc

https://www.losant.com

