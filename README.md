# 개요
FastAPI 를 사용한 개인 프로젝트 용 간단한 API 서버입니다.
DockerFile 빌드 후 실행시키시면 `localhost:8000/docs` 에서 api 설명을 보실 수 있습니다.

# 실행
### 도커 이미지 빌드
```bash
docker build -t api
```

### 도커 실행
```bash
docker run --rm -p 8000:8080 api
```