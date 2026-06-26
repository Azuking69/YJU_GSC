# 1) 빌드 스테이지 — React 앱 즉석 생성·빌드
FROM node:20-alpine AS builder
WORKDIR /app
RUN npx --yes create-react-app myapp && cd myapp && npm run build
# 2) 실행 스테이지 — Nginx만 포함
FROM nginx:alpine
COPY --from=builder /app/myapp/build /usr/share/nginx/html
EXPOSE 80