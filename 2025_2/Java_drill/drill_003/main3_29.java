package Java_drill.drill_003;

import java.util.Scanner;

public class main3_29 {
    public static void main(String[] args) {
        // 입력 준비
        Scanner scanner = new Scanner(System.in);
        
        try{
        // 입력 내용 표지    
        System.out.println("정수를 입력하세요: ");
        // 입력 받기
        int num = scanner.nextInt();        
        // int -> byte 바꾸기
        byte bytenum = (byte) num;
        // overflow, underflow 판단
            if (num == bytenum){
                System.out.println("오바플로우 또는 안더플로우는 발생하지 않습니다.");
                System.out.println("byte 값: " + bytenum);
            } else {
                System.out.println("오바플로우 또는 안더플로우가 발생했습니다.");
            }
        } catch (java.util.InputMismatchException e){
            System.out.println("오류: 정수를 입력하세요.");
        } finally {
            scanner.close();
        }
    }
}
