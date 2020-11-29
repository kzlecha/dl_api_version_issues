-- Reading all Libraries
/*
    this was the initial query used, however, since Stack Exchange has a limit
    on what can be returned, separating the query returned more results
*/

SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags,
  P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId

WHERE
  (lower(P.Tags) LIKE '%keras%'
   OR lower(P.Tags) LIKE '%tensorflow%'
   OR lower(P.Tags) LIKE '%tesseract%'
   OR lower(P.Tags) LIKE '%pytorch%'
   OR lower(P.Tags) LIKE '%pyspark%'
   OR lower(P.Tags) LIKE '%theano%'
   OR lower(P.Tags) LIKE '%caffe%'
   
   )
;

-- Gathering all data
/*
    this used too many resources to run directly
*/

SELECT
  Posts.CreationDate,
  Posts.Score,
  Posts.ViewCount,
  Posts.Body,
  Posts.Title,
  Posts.Tags,
  Posts.AnswerCount,
  Posts.CommentCount,
  Posts.FavoriteCount
  
FROM
  Posts
  
WHERE
  (Tags LIKE '%keras%'
   OR Tags LIKE '%tensorflow%'
   OR Tags LIKE '%tesseract%'
   OR Tags LIKE '%pytorch%'
   OR Tags LIKE '%pyspark%'
   )
   AND (Body LIKE '%HiveContext%'
        OR Body LIKE '%TensorFloat-32%'
        OR Body LIKE '%TF_StringDecode%'
         OR Body LIKE '%TF_StringEncode%'
         OR Body LIKE '%TessBaseAPI::DumpPGM%'
         OR Body LIKE '%WriteOldConfigFile%'
         OR Body LIKE '%WriteOldProtoFile%'
         OR Body LIKE '%torch.save%'
         OR Body LIKE '%Variable%'
         OR Body LIKE '%SQLContext%'
         OR Body LIKE 'Tess4j'
         )
;