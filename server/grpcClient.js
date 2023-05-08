import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";

const packageDefinition = protoLoader.loadSync("recognition.proto", {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const recognitionProto = grpc.loadPackageDefinition(packageDefinition).recognition;

const grpcClient = new recognitionProto.Recognizer("localhost:50051", grpc.credentials.createInsecure());

export { grpcClient };
