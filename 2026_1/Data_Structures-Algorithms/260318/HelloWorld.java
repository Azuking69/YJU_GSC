package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

    @RestController
    public class HelloWorld {

        @GetMapping("login")
        public String login(String id, String pass){
            String str = id+"니은"+"로그인 되었습니다";
            return str;
        }

        @GetMapping("/hi")
        public  String hello(String x){
            String str = "2+1=2 , 2+2=4";
            return str;
        }

    }
