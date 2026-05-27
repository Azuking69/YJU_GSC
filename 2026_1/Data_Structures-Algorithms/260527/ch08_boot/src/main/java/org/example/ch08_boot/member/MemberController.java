package org.example.ch08_boot.member;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class MemberController {

    @GetMapping("/signUp")
    public String signUp(){
        return "sign_up";
    }

    @PostMapping("/signUpConfirm")
    public String signUpConfirm(@RequestParam String m_id,
                                @RequestParam String m_pw,
                                @RequestParam String m_mail,
                                @RequestParam String m_phone
    ){
        System.out.println(m_id);
        System.out.println(m_pw);
        System.out.println(m_mail);
        System.out.println(m_phone);
        return "sign_up_ok";
    }
}
