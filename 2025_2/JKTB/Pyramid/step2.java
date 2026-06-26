package JKTB.Pyramid;

// 以下のように表示されること
// #####
// #####
// #####
// #####
// #####

public class step2 {
    public static void main(String[] args) {
        // 행
        for(int i = 0; i < 5; i++){
            // 열
            for(int j = 0; j < 5; j++){
                System.out.print("#");
            }
            // そのあと改行する
            System.out.println();
        }
    }
}
