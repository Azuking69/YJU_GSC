package org.example.ch8_boot.member;

import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class MemberService {

    /*
     * 기존 코드에서는 MemberDao를 주입받아 JDBC Template으로 DB를 사용했다.
     *
     * 변경 후에는 MemberRepository를 주입받는다.
     * - MemberRepository는 Spring Data JPA가 자동으로 구현 객체를 만들어준다.
     * - 개발자는 인터페이스만 만들고, save/findById/existsById 같은 메소드를 호출하면 된다.
     *
     * 기존 REST Controller, MVC Controller 코드는 그대로 MemberService를 호출한다.
     * 즉, Controller 입장에서는 내부가 JDBC에서 JPA로 바뀌었는지 거의 알 필요가 없다.
     */
    private final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    public boolean signUpConfirm(MemberVo memberVo) {
        System.out.println("[MemberService] signUpConfirm()");

        /*
         * 1. 기본 검증
         * - 화면 또는 REST API에서 넘어온 값이 없으면 회원가입 실패 처리한다.
         */
        if (memberVo == null) {
            return false;
        }

        if (isBlank(memberVo.getM_id()) || isBlank(memberVo.getM_pw())) {
            return false;
        }

        /*
         * 2. 중복 아이디 확인
         *
         * 기존 JDBC 코드:
         * - memberDao.existsById(memberVo.getM_id())
         * - 내부에서 SELECT COUNT(*) SQL을 직접 작성했다.
         *
         * JPA 변경 후:
         * - memberRepository.existsById(memberVo.getM_id())
         * - JpaRepository가 기본 제공하는 메소드다.
         * - 실제로는 PK 기준 존재 여부를 확인하는 SQL이 실행된다.
         */
        if (memberRepository.existsById(memberVo.getM_id())) {
            return false;
        }

        /*
         * 3. MemberVo -> MemberEntity 변환
         *
         * MemberVo는 화면/JSON 데이터를 담는 객체이고,
         * MemberEntity는 DB 테이블과 연결되는 객체다.
         *
         * 그래서 DB에 저장하기 전에 Entity로 바꿔준다.
         */
        MemberEntity memberEntity = toEntity(memberVo);

        /*
         * 4. 저장
         *
         * 기존 JDBC 코드:
         * - INSERT INTO member (...) VALUES (?, ?, ?, ?)
         * - jdbcTemplate.update(...)
         *
         * JPA 변경 후:
         * - memberRepository.save(memberEntity)
         *
         * save()는 PK 값이 새 값이면 INSERT처럼 동작한다.
         * 이미 존재하는 PK이면 UPDATE처럼 동작할 수 있다.
         * 여기서는 위에서 existsById()로 중복 검사를 했기 때문에 회원가입 시 INSERT 용도로 이해하면 된다.
         */
        memberRepository.save(memberEntity);

        printAllMember();
        return true;
    }

    public boolean signInConfirm(MemberVo memberVo) {
        System.out.println("[MemberService] signInConfirm()");

        if (memberVo == null) {
            return false;
        }

        if (isBlank(memberVo.getM_id()) || isBlank(memberVo.getM_pw())) {
            return false;
        }

        /*
         * 회원 한 명 조회
         *
         * 기존 JDBC 코드:
         * - memberDao.selectMember(memberVo.getM_id())
         * - SELECT ... FROM member WHERE m_id = ? SQL을 직접 작성했다.
         *
         * JPA 변경 후:
         * - memberRepository.findById(memberVo.getM_id())
         * - PK 기준으로 한 명을 조회한다.
         *
         * findById()의 반환 타입은 Optional<MemberEntity>이다.
         * - 조회 성공: Optional 안에 MemberEntity가 들어 있다.
         * - 조회 실패: Optional이 비어 있다.
         *
         * null을 바로 반환하지 않고 Optional을 사용하는 이유는
         * "조회 결과가 없을 수 있다"는 사실을 코드에서 명확히 표현하기 위해서다.
         */
        Optional<MemberEntity> optionalMember = memberRepository.findById(memberVo.getM_id());

        if (optionalMember.isEmpty()) {
            return false;
        }

        MemberEntity savedMember = optionalMember.get();

        /*
         * 비밀번호 비교
         *
         * 기존 예제 흐름을 최대한 유지하기 위해 단순 문자열 비교를 그대로 사용한다.
         * 실무에서는 암호화된 비밀번호를 비교해야 한다.
         */
        return savedMember.getMPw().equals(memberVo.getM_pw());
    }

    private boolean isBlank(String value) {
        return value == null || value.trim().isEmpty();
    }

    /*
     * MemberVo -> MemberEntity 변환 메소드
     *
     * 이 변환 메소드를 따로 만든 이유:
     * - Controller와 REST API 쪽 코드는 기존 MemberVo를 그대로 사용한다.
     * - DB 저장에 필요한 부분만 Entity로 변환한다.
     * - 그래서 전체 코드 수정량이 줄어든다.
     */
    private MemberEntity toEntity(MemberVo memberVo) {
        return new MemberEntity(
                memberVo.getM_id(),
                memberVo.getM_pw(),
                memberVo.getM_mail(),
                memberVo.getM_phone()
        );
    }

    /*
     * 전체 회원 목록 출력
     *
     * 기존 JDBC MemberDao의 printAllMember()와 같은 실습 확인용 메소드다.
     * 실무에서는 Service에서 콘솔 출력은 잘 하지 않지만,
     * 학생들이 save() 이후 DB에 실제로 저장됐는지 확인하기 쉽게 남겨둔다.
     */
    private void printAllMember() {
        System.out.println("===== 전체 회원 목록 - JPA =====");

        /*
         * findAll()
         * - JpaRepository가 기본 제공하는 전체 조회 메소드다.
         * - 내부적으로 SELECT ... FROM member 형태의 SQL이 실행된다.
         */
        List<MemberEntity> memberList = memberRepository.findAll();

        if (memberList.isEmpty()) {
            System.out.println("등록된 회원이 없습니다.");
            return;
        }

        for (MemberEntity member : memberList) {
            System.out.println("m_id: " + member.getMId());
            System.out.println("m_pw: ****");
            System.out.println("m_mail: " + member.getMMail());
            System.out.println("m_phone: " + member.getMPhone());
            System.out.println("------------------------");
        }
    }
}
