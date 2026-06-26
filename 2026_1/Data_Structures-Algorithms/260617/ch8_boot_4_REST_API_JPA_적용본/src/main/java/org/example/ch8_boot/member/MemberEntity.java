package org.example.ch8_boot.member;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/*
 * MemberEntity
 *
 * JPA에서 DB 테이블과 연결되는 클래스다.
 * 기존 코드의 MemberVo는 화면/Form/JSON 데이터를 담는 용도로 그대로 둔다.
 *
 * 왜 MemberVo를 바로 Entity로 바꾸지 않았나?
 * - 코드 수정량을 줄이고, 수업 때 역할을 구분해서 설명하기 위해서다.
 * - MemberVo     : 화면 또는 REST API 요청/응답에서 사용하는 데이터 객체
 * - MemberEntity : DB 테이블과 직접 연결되는 JPA 객체
 *
 * @Entity
 * - 이 클래스가 JPA 관리 대상임을 의미한다.
 * - 쉽게 말하면 "이 클래스 객체를 DB 테이블의 한 행(row)처럼 다룰 수 있다"는 뜻이다.
 *
 * @Table(name = "member")
 * - 이 Entity가 MariaDB의 member 테이블과 연결된다는 뜻이다.
 * - 기존 JDBC 예제에서 사용하던 테이블 이름을 그대로 사용한다.
 */
@Entity
@Table(name = "member")
public class MemberEntity {

    /*
     * @Id
     * - 이 필드가 PRIMARY KEY라는 뜻이다.
     * - 기존 member 테이블에서 m_id가 회원을 구분하는 기본키 역할을 한다.
     *
     * @Column(name = "m_id")
     * - 자바 필드명은 mId처럼 쓰고,
     *   실제 DB 컬럼명은 기존 테이블 구조에 맞춰 m_id로 연결한다.
     * - nullable = false : 반드시 값이 있어야 한다.
     * - length = 50      : VARCHAR 길이 힌트다. ddl-auto=update 사용 시 참고된다.
     */
    @Id
    @Column(name = "m_id", nullable = false, length = 50)
    private String mId;

    /*
     * 비밀번호 컬럼
     *
     * 주의:
     * - 지금 예제는 JPA 핵심 흐름을 보여주기 위한 수업용 코드라서
     *   비밀번호를 그대로 저장한다.
     * - 실제 서비스에서는 BCrypt 같은 방식으로 반드시 암호화해서 저장해야 한다.
     */
    @Column(name = "m_pw", nullable = false, length = 100)
    private String mPw;

    @Column(name = "m_mail", length = 100)
    private String mMail;

    @Column(name = "m_phone", length = 30)
    private String mPhone;

    /*
     * JPA 기본 생성자
     * - JPA가 Entity 객체를 만들 때 기본 생성자를 사용한다.
     * - 그래서 Entity 클래스에는 기본 생성자가 필요하다.
     */
    public MemberEntity() {
    }

    public MemberEntity(String mId, String mPw, String mMail, String mPhone) {
        this.mId = mId;
        this.mPw = mPw;
        this.mMail = mMail;
        this.mPhone = mPhone;
    }

    public String getMId() {
        return mId;
    }

    public void setMId(String mId) {
        this.mId = mId;
    }

    public String getMPw() {
        return mPw;
    }

    public void setMPw(String mPw) {
        this.mPw = mPw;
    }

    public String getMMail() {
        return mMail;
    }

    public void setMMail(String mMail) {
        this.mMail = mMail;
    }

    public String getMPhone() {
        return mPhone;
    }

    public void setMPhone(String mPhone) {
        this.mPhone = mPhone;
    }
}
