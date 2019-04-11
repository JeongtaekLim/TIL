# Elasticsearch
### NRT(Near Real Time)
약 1초 만에 검색함
### Cluster
### Node
### Document
- Document is basic unit of information
- 1TB분량의 documents가 1개 index에 1개 node에 위치하면 안된다. 느림. index를 쪼개서 사용하는것이 shard
- 기본적으로, 각 index는 5개의 primary shard와, 1개의 replica로 이루어진다.