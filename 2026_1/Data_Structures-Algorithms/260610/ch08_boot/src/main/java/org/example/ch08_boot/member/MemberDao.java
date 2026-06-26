package org.example.ch08_boot.member;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import java.util.List;


@Repository
public class MemberDao {
    private final JdbcTemplate jdbcTemplate;

    public MemberDao(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }
    public boolean existsById(String m_id) {
        if(m_id == null) {
            return false;
        }
        String sql = """
                SELECT COUNT(*)
                FROM member
                WHERE m_id = ?
                """;
        Integer count = jdbcTemplate.queryForObject(
                sql,
                Integer.class,
                m_id
        );
        return count != null && count > 0;
    }

    public boolean insertMember(MemberVo memberVo) {
        System.out.println("[MemberDao] insertMember()");

        if (memberVo == null || memberVo.getM_id() == null) {
            return false;
        }

        String sql = """
                INSERT INTO member
                (m_id, m_pw, m_mail, m_phone)
                VALUES (?, ?, ?, ?)
                """;

        try{
            int result = jdbcTemplate.update(
              sql,
              memberVo.getM_id(),
              memberVo.getM_pw(),
              memberVo.getM_mail(),
              memberVo.getM_phone()
            );
            printAllMember();
            return result > 0;

        } catch (RuntimeException e) {
            System.out.println("[MemberDao] 이미 존재하는 아이디입니다." + memberVo.getM_id());
            return false;
        }
    }

    public MemberVo selectMember(String m_id){
        System.out.println("[MemberDao] selectMember()");

        if(m_id == null) {
            return null;
        }

        String sql = """
                SELECT m_id, m_pw, m_mail, m_phone
                FROM member
                WHERE m_id = ?
        """;

        return jdbcTemplate.query(
                sql,
                rs -> {
                    if(rs.next()) {
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

    private void printAllMember() {
        System.out.println("===== 전체 회원 목록");

        String sql = """
                SELECT m_id, m_pw, m_mail, m_phone
                FROM member
                ORDER BY m_id
                """;

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

        if(memberList.isEmpty()) {
            System.out.println("등록된 회원이 없습니다.");
            return;
        }

        for (MemberVo member : memberList) {
            System.out.println("m_id: " + member.getM_id());
            System.out.println("m_pw: ****");
            System.out.println("m_mail: " + member.getM_mail());
            System.out.println("m_phone: " + member.getM_phone());
            System.out.println("----------------------");

        }
    }
}
