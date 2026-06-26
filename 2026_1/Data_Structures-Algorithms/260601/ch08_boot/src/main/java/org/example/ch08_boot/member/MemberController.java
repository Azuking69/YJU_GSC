package org.example.ch08_boot.member;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class MemberController {

    @GetMapping("/signUp")
    public String signUp(Model model){
        model.addAttribute("memberVo", new MemberVo());
        return "sign_up";
    }

    @PostMapping("/signUpConfirm")
    public String signUpConfirm(MemberVo memberVo){
        System.out.println(memberVo.getM_id());
        System.out.println(memberVo.getM_pw());
        System.out.println(memberVo.getM_mail());
        System.out.println(memberVo.getM_phone());
        return "sign_up_ok";
    }
}
