package ch03_pjt_01;

import org.springframework.context.support.GenericXmlApplicationContext;

public class MainClass {
    public static void main(String[] args){

//        개발자인 우리가 직접 객체화
//        TransportationWalk transportationWalk = new TransportationWalk();
//        transportationWalk.move();

//        applicationContext.xml 를 사용해서 객체화
        GenericXmlApplicationContext ctx
                = new GenericXmlApplicationContext("classpath:applicationContext.xml");

        TransportationWalk transportationWalk = ctx.getBean("tWalk", TransportationWalk.class);
        transportationWalk.move();

        ctx.close();
    }
}
