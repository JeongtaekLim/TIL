# SavedModel

https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md

SavedModel 이란, TensorFlow 모델의 universal serialization format이다.
A SavedModel directory has the following structure:

```
assets/
assets.extra/
variables/
    variables.data-?????-of-?????
    variables.index
saved_model.pb
```
