# Downsample
Downsamples (or decimates) buckets of data points into a single value. As data is streamed into this node, each time `Bucket Size` points have been received, it will output a single data point based on the specified `Downsample Technique`. This node is useful for filtering high-frequency data.

## Input Configuration
* `Bucket Size`: The number of data points to process before returning a downsampled value.
* `Downsample Technique`: How to downsample the received data. `MEAN` returns the average of all data points in the bucket. `FIRST` returns the first data point received in each bucket. `LAST` returns the last data point in each bucket.
* `Downsample Identifier`: Optional identifier that allows this node to downsample multiple sets of data.
* `Value`: The incoming value that will be downsampled in each bucket.

## Output Result
This node will take the true path each time `Bucket Size` points have been processed and the output will be the downsampled value based on the specified technique. All other data points will result in the false path and the raw value will be directly passed through.

## Version History

| Version | Date | Description |
| ------- | -------- | ---------------- |
| v1.0.0  | 8/5/2018 | Initial release. |

---

This node was developed by [Losant](https://www.losant.com). Please place issues, comments, or questions on the [Losant Forums](https://forums.losant.com).

Copyright © 2018 Losant IoT, Inc

https://www.losant.com

