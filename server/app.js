import express from "express";
import multer from "multer";
import { ResponseDTO } from "./dtos/ResponseDTO.js";
import { grpcClient } from "./grpcClient.js";

const app = express();
const upload = multer({ storage: multer.memoryStorage() });

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post("/image", upload.single("image"), (req, res) => {
  const { name } = req.headers;
  if (!name) return res.status(400).json(new ResponseDTO(400, "Name is required"));

  const image = req.file.buffer.toString("base64");

  grpcClient.SendMessage({ name, image }, function (err, response) {
    if (err) return res.status(500).json(new ResponseDTO(500, "Internal Server error"));
    return res.json(new ResponseDTO(200, response.message));
  });
});

app.listen(3000, () => {
  console.log("Node.js server started at port 3000 ");
});
