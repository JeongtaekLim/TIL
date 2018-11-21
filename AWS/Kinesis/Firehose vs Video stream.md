# Firehose vs Video stream

## Intro

https://www.sumologic.com/blog/devops/kinesis-streams-vs-firehose/
2013년 12월 출시

Kinesis acts as a highly available conduit to stream messages between data producers and data consumers.
키네시스는 데이터 생산자, 데이터 소비자간 고가용 스트림메시지 수도관 역할을 한다.

The basic unit of scale when working with streams is a shard
스트림을 다룰때, 알아야할 가장 최소단위는 샤드이다.

Shards scale linearly, so adding shards to a stream will add 1MB per second of ingestion, and emit data at a rate of 2MB per second for every shard added.
샤드는 선형으로 스케일업되기때문에 샤드 하나를 추가할때마다 1Mbps 데이터 삽입속도가 증가하고, 2Mbps 데이터 방출속도가 증가한다.

Ten shards will scale a stream to handle 10MB (10,000 PUTs) of ingress, and 20MB of data egress per second. 
10개의 샤드는 10Mbps 규모의 인풋 스트림을 다루고, 20Mbps 규모의 아웃풋 스트림을 다룬다.
-> 1,000 PUT당 1MB, 1 PUT당 1Kb

It is possible to dynamically add or remove shards from a stream using the AWS Streams API. This is called resharding.
AWS 스트림 API를 통해서, 샤드를 동적으로 추가/제거 할 수 있다. 이를 리샤딩(resharding)이라고 한다.

Resharding cannot be done via the AWS Console, and is considered an advanced strategy when working with Kinesis. 
리샤딩은 AWS 콘솔에서 이루어질수 없으며, advanced 전략으로 Kinesis를 운영하는 와중에 이루어져야한다.

Records are units of data stored in a stream and are made up of a sequence number, partition key, and a data blob. 
레코드(Record)는 스트림에 있는 데이터의 단위이며, sequence number, partition key, 그리고 data blob를 가진다.

Partition keys are used to identify different shards in a stream, and allow a data producer to distribute data across shards.
파티션키(Partition key)는 한개의 스트림에 존재하는 서로다른 샤드들을 구분할 때 사용되며, 데이터 생산자가 샤드들을에게 데이터를 분배할때 사용된다.

Sequence numbers are unique identifiers for records inserted into a shard. They increase monotonically, and are specific to individual shards.
시퀀스넘버(Sequence number)는 샤드에 삽입되는 레코드들에 대한 고유한 구분자다. 단순증가하며, 각각 개별 샤드에 대해 고유하다.

## Kinesis Streams
Kinesis Streams is capable of capturing large amounts of data (terabytes per hour) from data producers, and streaming it into custom applications for data processing and analysis.

키네시스 스트림은 데이터 생산자로부터 시간당 테라바이트 그 이상의 큰 데이터를 소화해 낼 수 있고, 이 데이터를 커스텀 어플리케이션에 데이터프로세싱이나 분석을 위해 스트리밍 할 수 있다.

## Kinesis Firehose
Kinesis Firehose is Amazon’s data-ingestion product offering for Kinesis. It is used to capture and load streaming data into other Amazon services such as S3 and Redshift

Kinesis Firehose는 Kinesis를 위한 아마존의 데이터 섭취 제품이다. 이것은 스트리밍 데이터를 캡쳐 또는 로드하여 다른 AWS서비스(S3나 Redshift)로 보내는 역할을 한다.