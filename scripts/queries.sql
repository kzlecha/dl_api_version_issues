-- Keras

SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags, P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId
  
WHERE
  lower(P.Tags) LIKE '%keras%'

;

-- Tensorflow
SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags, P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId
  
WHERE
  lower(P.Tags) LIKE '%tensorflow%'
;

-- Tesseract
SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags, P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId
  
WHERE
  lower(P.Tags) LIKE '%tesseract%'
;

-- PyTorch
SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags, P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId
  
WHERE
  lower(P.Tags) LIKE '%pytorch%'

;

-- PySpark
SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags, P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId
  
WHERE
  lower(P.Tags) LIKE '%pyspark%'

;

-- Theano
SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags, P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId
  
WHERE
  lower(P.Tags) LIKE '%theano%'

;

-- Caffe
-- Note that this by nature includes caffe2
SELECT
  P.Id, P.CreationDate, P.Score, P.ViewCount, P.Body, P.Title, P.Tags, P.AnswerCount, P.CommentCount, P.ClosedDate,
  A.Id, A.CreationDate, A.Score, A.Body, A.CommentCount
FROM Posts P
LEFT OUTER JOIN Posts A
  ON A.PostTypeId = 2
  AND P.PostTypeId = 1
  AND P.Id = A.ParentId
  
WHERE
  lower(P.Tags) LIKE '%caffe%'

;