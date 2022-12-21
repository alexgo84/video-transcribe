echo on
curl -X POST \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@samples\IMG_9808.MP4;type=image/png' \
  127.0.0.1:8000/file2text/ 
