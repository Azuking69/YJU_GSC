package org.example.ch8_boot.member;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/*
 * REST API 전용 컨트롤러
 *
 * 기존 MemberController는 @Controller를 사용한다.
 * - 목적: HTML 화면을 보여주기
 * - 반환값: "sign_up_ok" 같은 템플릿 파일 이름
 *
 * 이 클래스는 @RestController를 사용한다.
 * - 목적: HTML 화면 이름이 아니라 JSON 데이터를 응답하기
 * - 반환값: MemberApiResult 객체
 * - 스프링 부트가 객체를 자동으로 JSON으로 바꿔서 브라우저에 보내준다.
 *
 * 기존 수업 코드의 흐름을 최대한 유지하기 위해
 * MemberService, MemberDao, MemberVo는 그대로 재사용한다.
 */
@RestController
@RequestMapping("/api/members")
public class MemberRestController {

    private final MemberService memberService;

    /*
     * 생성자 주입
     * - MemberService 객체는 스프링 컨테이너가 자동으로 넣어준다.
     * - 기존 MemberController와 같은 방식이다.
     */
    public MemberRestController(MemberService memberService) {
        this.memberService = memberService;
    }

    /*
     * REST 방식 회원가입 API
     *
     * 요청 주소:
     * POST /api/members/sign-up
     *
     * 요청 데이터 예시(JSON):
     * {
     *   "m_id": "hong",
     *   "m_pw": "1234",
     *   "m_mail": "hong@test.com",
     *   "m_phone": "010-1111-2222"
     * }
     *
     * @RequestBody
     * - 요청 본문(body)에 들어온 JSON 데이터를 MemberVo 객체로 변환해준다.
     * - 기존 form 방식에서는 input name 값이 MemberVo 필드에 자동 바인딩되었다.
     * - REST 방식에서는 JSON key 값이 MemberVo 필드에 자동 바인딩된다.
     */
    @PostMapping("/sign-up")
    public MemberApiResult signUp(@RequestBody MemberVo memberVo) {
        System.out.println("[MemberRestController] signUp()");
        System.out.println("memberVo = " + memberVo);

        boolean result = memberService.signUpConfirm(memberVo);

        if (result) {
            return new MemberApiResult(
                    true,
                    "회원가입에 성공했습니다.",
                    memberVo.getM_id()
            );
        }

        return new MemberApiResult(
                false,
                "회원가입에 실패했습니다. 아이디가 비어 있거나 이미 존재할 수 있습니다.",
                null
        );
    }

    /*
     * REST 방식 로그인 API
     *
     * 요청 주소:
     * POST /api/members/sign-in
     *
     * 요청 데이터 예시(JSON):
     * {
     *   "m_id": "hong",
     *   "m_pw": "1234"
     * }
     *
     * 기존 MVC 로그인과 차이점:
     * - 기존: 성공하면 sign_in_ok.html 화면으로 이동
     * - REST: 성공/실패 결과를 JSON으로 반환
     */
    @PostMapping("/sign-in")
    public MemberApiResult signIn(@RequestBody MemberVo memberVo) {
        System.out.println("[MemberRestController] signIn()");

        boolean result = memberService.signInConfirm(memberVo);

        if (result) {
            return new MemberApiResult(
                    true,
                    "로그인에 성공했습니다.",
                    memberVo.getM_id()
            );
        }

        return new MemberApiResult(
                false,
                "아이디 또는 비밀번호가 올바르지 않습니다.",
                null
        );
    }
}
