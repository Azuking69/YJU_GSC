package Java_drill.drill_002;

// Scanner import
import java.util.Scanner;

public class main2_3 {
    public static void main(String[] args) {
        // object 작성
        Scanner scanner = new Scanner(System.in);
        // プロンプト作成
        System.out.println("半径の入力: ");
        // 半径の入力を受け取り
        double num = scanner.nextDouble();
        // 계산
        double total = 3.14159 * num * num;
        // 출력
        System.out.println(total);
        // close
        scanner.close();
    }
}
