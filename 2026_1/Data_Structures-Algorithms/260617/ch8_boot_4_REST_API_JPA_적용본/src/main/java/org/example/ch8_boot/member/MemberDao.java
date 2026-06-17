package org.example.ch8_boot.member;

import org.springframework.dao.DuplicateKeyException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Repository
public class MemberDao {
    private final JdbcTemplate jdbcTemplate;
    //생성자가 하나만 있는 경우 @Autowired 생략 가능(부트 기준 1.5, 스프링기준 4.3 이상부터 적용)
    public MemberDao(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }
    public boolean existsById(String m_id) {
        // 아이디가 null이면 DB 조회할 필요 없이 false 처리
        if (m_id == null) {
            return false;
        }
        String sql = """
                SELECT COUNT(*)
                FROM member
                WHERE m_id = ?
                """;
        /*
         * queryForObject()
         * - SELECT 결과가 값 하나일 때 사용 , query()메소드는 결과가 여러개일때 사용
         * - 여기서는 COUNT(*) 결과를 Integer로 받는다.
         * ? 자리에는 아래 m_id 값이 들어간다.  -> placeholder 방식 사용
         */
        //JdbcTemplate은 PreparedStatement을 사용해서 SQL / Parameter를 분리해줌
        //이로 인해 SQL Injection 등의 방지 가능
        Integer count = jdbcTemplate.queryForObject(
                sql,
                Integer.class,
                m_id
        );
        return count != null && count > 0;
    }
    /*
     * 회원가입 처리
     * 기존 코드:
     * - memberDB.put(memberVo.getM_id(), memberVo)
     * 변경 후:
     * - INSERT SQL을 실행해서 MariaDB member 테이블에 저장
     */
    public boolean insertMember(MemberVo memberVo) {
        System.out.println("[MemberDao] insertMember()");
        /*
         * 최소 검증
         * - memberVo 자체가 없거나
         * - 아이디가 없으면 저장 불가
         */
        if (memberVo == null || memberVo.getM_id() == null) {
            return false;
        }
        // """   텍스트 블록임돠~
        String sql = """
                INSERT INTO member
                (m_id, m_pw, m_mail, m_phone)
                VALUES (?, ?, ?, ?)
                """;
        try {
            /*
             * update()
             * - INSERT, UPDATE, DELETE 실행할 때 사용
             * - 반환값은 영향을 받은 행의 개수
             * 아래 값들이 SQL의 ? 자리에 순서대로 들어간다.
             */
            int result = jdbcTemplate.update(  //데이터변경 -> insert, update, delete 전부 update() 메소드로 처리
                    sql,
                    memberVo.getM_id(),
                    memberVo.getM_pw(),
                    memberVo.getM_mail(),
                    memberVo.getM_phone()
            );
            printAllMember();
            return result > 0;

        } catch (DuplicateKeyException e) {
            /*
             * m_id는 PRIMARY KEY이므로
             * 이미 같은 아이디가 있으면 중복 키 오류가 발생한다.
             */
            System.out.println("[MemberDao] 이미 존재하는 아이디입니다: " + memberVo.getM_id());
            return false;
        }
    }
    /*
     * 회원 한 명 조회
     * 기존 코드:
     * - memberDB.get(m_id)
     * 변경 후:
     * - MariaDB에서 m_id에 해당하는 회원 한 명을 SELECT
     */
    public MemberVo selectMember(String m_id) {
        System.out.println("[MemberDao] selectMember()");
        if (m_id == null) {
            return null;
        }
        String sql = """
                SELECT m_id, m_pw, m_mail, m_phone
                FROM member
                WHERE m_id = ?
                """;
        /*
         * query()
         * - SELECT 결과를 조회할 때 사용
         * - ResultSet을 직접 다루면서 MemberVo 객체로 변환한다.
         *
         * rs.next()
         * - 조회 결과가 있으면 true
         * - 없으면 false
         */
        return jdbcTemplate.query(    //요놈의 결과는 ResultSet이 아니다. 람다식의 결과물이 리턴값
                sql,
                rs -> {    //람다식 (rs) -> {} 매개변수 하나일 때 괄호 생략
                    if (rs.next()) {
                        MemberVo memberVo = new MemberVo();

                        memberVo.setM_id(rs.getString("m_id"));
                        memberVo.setM_pw(rs.getString("m_pw"));
                        memberVo.setM_mail(rs.getString("m_mail"));
                        memberVo.setM_phone(rs.getString("m_phone"));

                        return memberVo;
                    }
                    return null;
                },
                m_id
        );
    }

    /*
     * 전체 회원 목록 출력
     * 기존 코드:
     * - memberDB.forEach(...)
     * 변경 후:
     * - MariaDB member 테이블에서 전체 회원을 SELECT해서 콘솔에 출력
     * 실무에서는 DAO에서 콘솔 출력은 잘 하지 않지만,
     * 수업/실습용으로 DB에 저장됐는지 확인하기 위해...
     */
    private void printAllMember() {
        System.out.println("===== 전체 회원 목록 =====");
        String sql = """
                SELECT m_id, m_pw, m_mail, m_phone
                FROM member
                ORDER BY m_id
                """;
        /*
         * query()
         * - 여러 행을 조회할 때 사용
         * - 각 행을 MemberVo 객체로 변환해서 List<MemberVo>로 받는다.
         */
        List<MemberVo> memberList = jdbcTemplate.query(
                sql,
                (rs, rowNum) -> {
                    MemberVo memberVo = new MemberVo();

                    memberVo.setM_id(rs.getString("m_id"));
                    memberVo.setM_pw(rs.getString("m_pw"));
                    memberVo.setM_mail(rs.getString("m_mail"));
                    memberVo.setM_phone(rs.getString("m_phone"));

                    return memberVo;
                }
        );

        if (memberList.isEmpty()) {
            System.out.println("등록된 회원이 없습니다.");
            return;
        }

        for (MemberVo member : memberList) {
            System.out.println("m_id: " + member.getM_id());
            System.out.println("m_pw: ****");
            System.out.println("m_mail: " + member.getM_mail());
            System.out.println("m_phone: " + member.getM_phone());
            System.out.println("------------------------");
        }
    }

}
