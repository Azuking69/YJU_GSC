package org.example.ch8_boot.member;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class MemberController {
    private final MemberService memberService;
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
    @PostMapping("/signUpConfirm")
    public String signUpConfirm(MemberVo memberVo ) {
        System.out.println("[MemberController] signUpConfirm()");
        System.out.println("memberVo = " + memberVo);
        boolean result = memberService.signUpConfirm(memberVo);
        if (result) {
            return "sign_up_ok";
        }
        return "sign_up_ng";
    }
    @GetMapping("/signUp")
    public String signUp(Model model) {
        model.addAttribute("memberVo", new MemberVo());
        return "sign_up";
    }

    @GetMapping("/signIn")
    public String signIn(Model model) {
        model.addAttribute("memberVo", new MemberVo());
        return "sign_in";
    }

    @PostMapping("/signInConfirm")
    public String signInConfirm(MemberVo memberVo, Model model) {
        System.out.println("[MemberController] signInConfirm()");
        boolean result = memberService.signInConfirm(memberVo);

        if (result) {
            model.addAttribute("memberId", memberVo.getM_id());
            return "sign_in_ok";
        }
        return "sign_in_ng";
    }
}
