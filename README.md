# gRPC node / python

### Para compilar o arquivo proto e usar no python, basta rodar o comando na root

    python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. recognition.proto
