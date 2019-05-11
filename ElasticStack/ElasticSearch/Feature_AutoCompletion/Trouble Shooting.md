# Trouble Shooting

## property 속성 변경
다음과 같은 요청을 보내니
```
PUT used_car/_mapping/doc
{
  "properties": {
    "brand": {
      "type": "completion"
    }
  }
}
```
아래 응답이 왔다.
```
{
  "error": {
    "root_cause": [
      {
        "type": "illegal_argument_exception",
        "reason": "mapper [brand] of different type, current_type [text], merged_type [completion]"
      }
    ],
    "type": "illegal_argument_exception",
    "reason": "mapper [brand] of different type, current_type [text], merged_type [completion]"
  },
  "status": 400
}
```
결론적으로 Completion suggester는 indexing 시점에만 작용할 수 있으므로,
jdbc-input-plugin을 사용하는 경우에는 쓸 수 없다.
만약 사용하고 싶다면, jdbc-input-plugin으로 생성된 documents들을 reindexing 해서 새로운 index를 생성해서 쓰면 되지만,
좀더 느리더라도 추가 작업이 필요없을것으로 판단되는 `edge_ngram` 방법으로 방향을 틀었다.
(이후에, 결국 깔끔하게 reindexing하는 방법을 사용했다.;)
