#!/bin/bash
APP_NAME="protos"
MODULE_NAME="product"
PROTO_DIR=$APP_NAME/$MODULE_NAME
echo "Generate gRPC code"

NEW_FILE_NAME="brand"
python -m grpc_tools.protoc \
  --proto_path=. \
  --python_out=. --grpc_python_out=. \
  $PROTO_DIR/$NEW_FILE_NAME.proto

NEW_FILE_NAME="notification"
python -m grpc_tools.protoc \
  --proto_path=. \
  --python_out=. --grpc_python_out=. \
  $PROTO_DIR/$NEW_FILE_NAME.proto

NEW_FILE_NAME="product"
python -m grpc_tools.protoc \
  --proto_path=. \
  --python_out=. --grpc_python_out=. \
  $PROTO_DIR/$NEW_FILE_NAME.proto

NEW_FILE_NAME="productGroup"
python -m grpc_tools.protoc \
  --proto_path=. \
  --python_out=. --grpc_python_out=. \
  $PROTO_DIR/$NEW_FILE_NAME.proto