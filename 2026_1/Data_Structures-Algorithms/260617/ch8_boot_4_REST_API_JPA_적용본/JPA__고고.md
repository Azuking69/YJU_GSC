# ch8_boot REST API 예제 - JPA 적용본

## 변경 목표

기존 REST API 회원가입/로그인 흐름은 최대한 유지하고, DB 접근 방식만 JDBC Template에서 JPA로 바꾼 예제입니다.

기존 흐름:

```text
Controller / RestController → MemberService → MemberDao → JdbcTemplate → MariaDB
```

변경 후 흐름:

```text
Controller / RestController → MemberService → MemberRepository → JPA/Hibernate → MariaDB
```

## 핵심 변경 파일

### 1. pom.xml

`spring-boot-starter-data-jpa` 의존성을 추가했습니다.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

### 2. application.properties

JPA 설정을 추가했습니다.

```properties
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.database-platform=org.hibernate.dialect.MariaDBDialect
```

### 3. MemberEntity.java 추가

`member` 테이블과 연결되는 JPA Entity 클래스입니다.

기존 `MemberVo`를 바로 Entity로 바꾸지 않은 이유는 코드 수정량을 줄이고, 수업에서 역할을 구분해서 설명하기 위해서입니다.

- `MemberVo`: 화면/Form/JSON 데이터 전달용
- `MemberEntity`: DB 테이블 연결용

### 4. MemberRepository.java 추가

`JpaRepository<MemberEntity, String>`를 상속받는 JPA Repository입니다.

기본 제공 메소드:

- `save()` : 저장
- `findById()` : PK 기준 조회
- `existsById()` : PK 존재 여부 확인
- `findAll()` : 전체 조회

### 5. MemberService.java 수정

기존에는 `MemberDao`를 사용했지만, 이제는 `MemberRepository`를 사용합니다.

기존 Controller와 REST Controller는 그대로 둡니다.

## 기존 MemberDao는 왜 남겨두었나?

JDBC Template 방식과 JPA 방식을 비교해서 설명할 수 있도록 삭제하지 않았습니다.

다만 현재 실행 흐름에서는 `MemberService`가 `MemberRepository`를 사용하므로 회원가입/로그인은 JPA 방식으로 처리됩니다.

## 주의사항

현재 예제는 수업용이라 비밀번호를 평문으로 저장합니다.
실제 서비스에서는 반드시 BCrypt 같은 방식으로 비밀번호를 암호화해야 합니다.
자 이제 열심히 달려봅시다. 