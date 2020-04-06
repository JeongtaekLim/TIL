# Query

### Sort

```
db.getCollection('my_collection').find({}).sort({_id: -1})
```

### Date filter

https://www.tutorialspoint.com/find-objects-between-two-dates-in-mongodb

```
db.order.find({"OrderDateTime":{ $gte:ISODate("2019-02-10"), $lt:ISODate("2019-02-21") }}).pretty();

```
