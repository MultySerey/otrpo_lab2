import cv2
import sys


def detect_faces(image_path: str) -> None:
    # Загрузить изображение
    image = cv2.imread(image_path)

    if image is None:
        print(f"Не удалось загрузить изображение: {image_path}")
        return

    # Преобразовать изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Загрузить классификатор для распознавания лиц
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Найти лица на изображении
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Вывести результат
    print(f"Найдено {len(faces)} лиц")


def main() -> None:
    print(sys.argv)

    # if len(sys.argv) > 1:
    #     image_path = sys.argv[1]
    # else:
    #     image_path = "photo.jpg"  # Путь к изображению в репозитории по умолчанию

    # detect_faces(image_path)


if __name__ == "__main__":
    main()
