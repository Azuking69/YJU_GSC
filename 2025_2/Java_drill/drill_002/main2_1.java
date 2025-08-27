package Java_drill.drill_002;

// Scannerクラスをインポート
import java.util.Scanner;

public class main2_1 {
    public static void main(String[] args) {
        // インスタンスの作成
        Scanner scanner = new Scanner(System.in);
        // ユーザーに名前の入力を促すプロンプトを表示
        System.out.println("이름을 입력하세요: ");
        // ユーザーからの入力を受け取り、文字列変数に格納
        // String inputString = scanner.next();   次の単語を読み取る
        // int inputInt = scanner.nextInt();      // 整数を読み取る
        // String inputLine = scanner.nextLine(); // 一行分の文字列を読み取る
        String name = scanner.nextLine();
        // 挨拶メッセージを生成して表示
        System.out.println("Hello, " + name + "!");
        // Scannerのクローズ
        scanner.close();
    }
}
