# Order: Search and Filter? Filter and Search?

https://www.elastic.co/kr/blog/elasticsearch-query-execution-order

* cost(): Approximation of how many documents the query/filter matches.
* docID(): The current doc ID, initialized at -1.
* advance(target): Find the first document beyond target that might match.
* nextDoc(): Find the next (in doc id order) doc that might match. This is an optimized version of advance(docID() + 1).
* matches(): Check whether the current document matches.
* matchCost(): An estimation of the cost of calling matches.
* score(): Compute the score of the current document.

