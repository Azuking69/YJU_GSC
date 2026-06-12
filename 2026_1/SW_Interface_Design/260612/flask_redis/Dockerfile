# Python 런타임이 포함된 가벼운 베이스 이미지
FROM python:3.12-slim
WORKDIR /app

# 의존성을 먼저 설치하여 캐시 효율 극대화
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드는 마지막에 복사 (자주 바뀌므로)
COPY . .
# 기본 Redis 호스트명을 환경 변수로 설정
ENV REDIS_HOST=redis REDIS_PORT=6379
EXPOSE 5000

# 컨테이너 시작 시 Flask 앱 실행
CMD ["python", "app.py"]