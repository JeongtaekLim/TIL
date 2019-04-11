# Access Kibana
Kibana is an open source analytics and visualization platform designed to search, view, and interact with data stored in Elasticsearch indices. The use of Kibana is included with your subscription.

In production systems, you might need to control what Elasticsearch data users can access through Kibana, so you need create credentials that can be used to access the necessary Elasticsearch resources. This means granting read access to the necessary indexes, as well as access to update the .kibana index.