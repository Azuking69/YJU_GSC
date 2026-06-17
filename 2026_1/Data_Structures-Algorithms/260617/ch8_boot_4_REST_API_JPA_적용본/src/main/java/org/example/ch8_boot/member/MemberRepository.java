package org.example.ch8_boot.member;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/*
 * MemberRepository
 *
 * JPA에서 DB 작업을 담당하는 인터페이스다.
 * 기존 JDBC Template 예제의 MemberDao와 비슷한 역할을 한다.
 *
 * 기존 MemberDao에서는 직접 SQL을 작성했다.
 * 예)
 * SELECT COUNT(*) FROM member WHERE m_id = ?
 * INSERT INTO member ...
 * SELECT ... FROM member WHERE m_id = ?
 *
 * JPA Repository를 사용하면 기본적인 CRUD SQL을 직접 작성하지 않아도 된다.
 * Spring Data JPA가 메소드 이름과 Entity 정보를 보고 필요한 SQL을 대신 만들어 실행한다.
 *
 * JpaRepository<MemberEntity, String>
 * - 첫 번째 타입 MemberEntity : 어떤 Entity를 다룰 것인지
 * - 두 번째 타입 String       : @Id 필드의 자료형, 여기서는 m_id가 String
 *
 * 이 인터페이스만 만들어도 기본 메소드가 자동 제공된다.
 * - save(entity)       : INSERT 또는 UPDATE
 * - findById(id)       : PK로 한 명 조회
 * - existsById(id)     : PK 존재 여부 확인
 * - findAll()          : 전체 조회
 * - deleteById(id)     : PK 기준 삭제
 */
@Repository
public interface MemberRepository extends JpaRepository<MemberEntity, String> {
}
