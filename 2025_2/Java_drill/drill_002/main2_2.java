package Java_drill.drill_002;

// Scanner import
import java.util.Scanner;

public class main2_2 {
    public static void main(String[] args) {
        // Scanner オブジェクト作成
        Scanner scanner = new Scanner(System.in);
        // ユーザーに整数1の入力を促すメッセージを表示
        System.out.println("정수 1를 입력하세요: ");
        // 整数1の入力を受け取り
        int num1 = scanner.nextInt();
        // 整数2の入力
        System.out.println("정수 2를 입력하세요: ");
        int num2 = scanner.nextInt();
        // 整数1と整数2を加算して、合計を計算
        int total = num1 + num2;
        // 合計を画面に表示
        System.out.println(total);
        // Scannerをクローズ
        scanner.close();
    }
}
