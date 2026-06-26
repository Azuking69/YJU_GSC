package JKTB.Pyramid;

// ピラミッド形に出力せよ
//         #
//       ###
//     #####
//   #######
// #########

public class step4 {
    public static void main(String[] args) {
        // 5行を定義
        int num = 5;
        // 5行繰り返す
        for(int i = 1; i <= num; i++){
            // 各行のはじめに空白を (5(num) - i) 個出力する
            for(int j = 0; j < num - i; j++){
                System.out.print(" ");
            }

            for(int k = 0; k < 2 * i - 1; k++){
                System.out.print("#");
            }

            // 改行する
            System.out.println();
        }
    }
}
