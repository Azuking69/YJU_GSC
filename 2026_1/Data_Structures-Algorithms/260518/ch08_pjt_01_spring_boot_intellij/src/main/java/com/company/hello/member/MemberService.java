package com.company.hello.member;

import org.springframework.stereotype.Service;

@Service
public class MemberService {

    private final MemberDao memberDao;

    public MemberService(MemberDao memberDao) {
        this.memberDao = memberDao;
    }

    public boolean signUpConfirm(MemberVo memberVo) {
        System.out.println("[MemberService] signUpConfirm()");

        if (memberVo == null) {
            return false;
        }

        if (isBlank(memberVo.getM_id()) || isBlank(memberVo.getM_pw())) {
            return false;
        }

        if (memberDao.existsById(memberVo.getM_id())) {
            return false;
        }

        return memberDao.insertMember(memberVo);
    }

    public boolean signInConfirm(MemberVo memberVo) {
        System.out.println("[MemberService] signInConfirm()");

        if (memberVo == null) {
            return false;
        }

        if (isBlank(memberVo.getM_id()) || isBlank(memberVo.getM_pw())) {
            return false;
        }

        MemberVo savedMember = memberDao.selectMember(memberVo.getM_id());

        if (savedMember == null) {
            return false;
        }

        return savedMember.getM_pw().equals(memberVo.getM_pw());
    }

    private boolean isBlank(String value) {
        return value == null || value.trim().isEmpty();
    }
}
