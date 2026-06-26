package org.example.ch8_boot.member;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/*
 * REST API 테스트용 화면을 보여주는 컨트롤러
 *
 * 주의:
 * - 이 클래스는 REST API가 아니다.
 * - 단순히 fetch()를 사용하는 새 HTML 화면을 보여주기 위한 MVC 컨트롤러다.
 *
 * REST API 자체는 MemberRestController가 담당한다.
 */
@Controller
public class MemberRestPageController {

    /*
     * REST 회원가입 테스트 화면
     * 주소: /rest/signUp
     */
    @GetMapping("/rest/signUp")
    public String restSignUp() {
        return "sign_up_rest";
    }

    /*
     * REST 로그인 테스트 화면
     * 주소: /rest/signIn
     */
    @GetMapping("/rest/signIn")
    public String restSignIn() {
        return "sign_in_rest";
    }
}
