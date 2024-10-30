# Face Detection App

Это приложение на Python использует OpenCV для распознавания лиц на изображении.

## Как запустить

1. Склонируйте репозиторий:

```powershell
git clone https://github.com/username/repository.git
```

2. Соберите Docker-образ:

```powershell
docker build -t face-detection-app .
```

3. Запустите приложение:

```powershell
docker run -v ${pwd}:/app face-detection-app photo.jpg
```

Либо используйте изображение с DockerHub:

```powershell
docker run -v $(pwd):/app username/face-detection-app:latest photo.jpg
```
