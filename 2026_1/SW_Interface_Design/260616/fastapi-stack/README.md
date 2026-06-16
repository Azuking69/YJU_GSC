# Lab 12 — Nginx + FastAPI + Postgres + Redis

간단한 RESTful API 스택을 Docker Compose로 실행하는 실습 예제입니다.

## 구성
- **nginx**  : 리버스 프록시 (외부 8080 → 내부 web:8000)
- **web**    : FastAPI 앱 (items CRUD, Redis 캐싱)
- **db**     : PostgreSQL 16
- **redis**  : Redis 7 (조회 결과 10초 캐시)

## 실행
```bash
docker compose up -d --build      # 빌드 + 전체 기동
docker compose ps                 # 모든 서비스 healthy 확인
```

## 동작 확인
```bash
# 데이터 생성
curl -X POST localhost:8080/items -H "Content-Type: application/json" -d '{"name":"docker"}'

# 첫 조회 — DB에서 (source: db)
curl localhost:8080/items

# 재요청 — 10초간 Redis 캐시 (source: cache)
curl localhost:8080/items
```

## 정리
```bash
docker compose down -v            # 컨테이너 + 볼륨(pgdata)까지 삭제
```
