package JKTB.Pyramid;

// 次のような出力をせよ：
// #
// ##
// ###
// ####
// #####

public class step3 {
    public static void main(String[] args) {
        for(int i = 0 + 1; i < 5 + 1; i++){
            // 1行ごとに、#の数が増えていく
            for(int j = 0; j < i; j++){
                System.out.print("#");
            }
        // 出力のあとに改行する
        System.out.println();
        }
    }
}
