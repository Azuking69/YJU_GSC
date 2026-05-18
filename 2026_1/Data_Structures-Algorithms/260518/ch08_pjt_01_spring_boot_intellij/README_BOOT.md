# Ch08 Spring Boot 버전

기존 `ch08_pjt_01` Spring Legacy MVC 실습을 IntelliJ + Spring Boot + Thymeleaf 기준으로 변환한 프로젝트입니다.

## 실행 방법

1. IntelliJ에서 이 폴더를 `Open`으로 엽니다.
2. Maven 동기화가 끝날 때까지 기다립니다.
3. `src/main/java/com/company/hello/Ch08BootApplication.java`를 실행합니다.
4. 브라우저에서 아래 주소로 접속합니다.

```text
http://localhost:8090/hello/
```

## 테스트 주소

```text
홈          http://localhost:8090/hello/
회원가입    http://localhost:8090/hello/signUp
로그인      http://localhost:8090/hello/signIn
```

## 주요 변경점

- `war` 패키징 → `jar` 기반 Spring Boot 실행 구조
- 외부 Tomcat, `web.xml`, `servlet-context.xml` 제거
- JSP → Thymeleaf HTML 템플릿
- `src/main/webapp/WEB-INF/views` → `src/main/resources/templates`
- 필드 `@Autowired` → 생성자 주입
- `@Component` DAO → `@Repository` DAO
- 기존 8장의 `MemberVo`, `MemberService`, `MemberDao`, `Map` 저장 구조는 유지

## 주의

현재 회원 정보는 실제 DB가 아니라 메모리 `Map`에 저장됩니다. 애플리케이션을 재시작하면 회원 정보가 사라지므로 다시 회원가입 후 로그인해야 합니다.
