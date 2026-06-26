package JKTB.Pyramid;

// #を5つ横に並べる
// 出力例：#####
// ・#を5個出力したい
// ・1個ずつループで出せばよさそう
// ・1回出力するたびに、次の#を出す
// ・改行はいらない（1行で終わらせたい）


public class step1 {
    public static void main(String[] args) {
        // #を5回出力する
        for (int i = 0; i < 5; i++){
            // 改行しないで出力する
            System.out.print("#");
        }
    }
}