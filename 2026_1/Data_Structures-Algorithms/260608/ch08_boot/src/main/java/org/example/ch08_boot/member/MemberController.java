package org.example.ch08_boot.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class MemberController {
    private final MemberService memberService;

    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/signUp")
    public String signUp(Model model){
        model.addAttribute("memberVo", new MemberVo());
        return "sign_up";
    }

    @PostMapping("/signUpConfirm")
    public String signUpConfirm(MemberVo memberVo){
        System.out.println("[MemberService]signUpConfirm()");
        System.out.println("memberVo = "  + memberVo);
        boolean result = memberService.signUpConfirm(memberVo);
        if(result){
            return "sign_up_ok";
        }
        return "sign_up_ng";
    }

    @GetMapping("/signIn")
    public String signIn(Model model){
        model.addAttribute("memberVo", new MemberVo());
        return "sign_in";
    }

    @PostMapping("/signInConfirm")
    public String signConfirm(MemberVo memberVo,  Model model){
        System.out.println("[MemberController]signInConfirm()");
        boolean result = memberService.signInConfirm(memberVo);
        if(result){
            model.addAttribute("memberId", memberVo.getM_id());
            return "sign_in_ok";
        }
        return "sign_in_ng";
    }
}
