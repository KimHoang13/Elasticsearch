# Store the face 128-dimension in Elasticsearch
## Create the mapping
curl -XPUT "http://localhost:9200/faces" -H 'Content-Type: application/json' -d'
{
  "mappings" : {
      "properties" : {
        "face_name" : {
          "type" : "keyword"
        },
        "face_encoding" : {
          "type" : "dense_vector",
          "dims" : 128
        }
      }
    }
}
