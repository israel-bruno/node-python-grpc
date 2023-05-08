import cv2
import numpy as np
from base64 import b64decode
from face_recognition import face_encodings, compare_faces

knownFaces = []


def recognizeFace(name, base64image) -> str:
    imageArray = np.fromstring(b64decode(base64image), np.uint8)
    image = cv2.imdecode(imageArray, cv2.IMREAD_COLOR)
    faceEncodings = face_encodings(image)

    if not len(faceEncodings):
        return "Nenhum rosto encontrado na imagem"

    knownEncodings = [face[1] for face in knownFaces]

    for idx, encoding in enumerate(faceEncodings):
        result = compare_faces(knownEncodings, encoding)
        if not True in result:
            knownFaces.append((name, encoding))
            return "Rosto não conhecido encontrado, salvando registros"

        return f"Rosto conhecido encontrado. Nome: {knownFaces[idx][0]}"
