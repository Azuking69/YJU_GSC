package com.company.hello.member;

import org.springframework.stereotype.Repository;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Repository
public class MemberDao {

    private final Map<String, MemberVo> memberDB = new ConcurrentHashMap<>();

    public boolean existsById(String m_id) {
        return memberDB.containsKey(m_id);
    }

    public boolean insertMember(MemberVo memberVo) {
        System.out.println("[MemberDao] insertMember()");

        if (memberVo == null || memberVo.getM_id() == null) {
            return false;
        }

        if (memberDB.containsKey(memberVo.getM_id())) {
            return false;
        }

        memberDB.put(memberVo.getM_id(), memberVo);
        printAllMember();

        return true;
    }

    public MemberVo selectMember(String m_id) {
        System.out.println("[MemberDao] selectMember()");
        return memberDB.get(m_id);
    }

    private void printAllMember() {
        System.out.println("===== 전체 회원 목록 =====");

        if (memberDB.isEmpty()) {
            System.out.println("등록된 회원이 없습니다.");
            return;
        }

        memberDB.forEach((id, member) -> {
            System.out.println("m_id: " + member.getM_id());
            System.out.println("m_pw: ****");
            System.out.println("m_mail: " + member.getM_mail());
            System.out.println("m_phone: " + member.getM_phone());
            System.out.println("------------------------");
        });
    }
}
