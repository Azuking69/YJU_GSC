package JKTB.ArrayList;

public class step1 {
    public static void main(String[] args) {
        // 配列作成
        int [] stocks = {10, 5, 3, 0, 8};

        //合計を入れる箱を作る
        int result = 0;

        for (int i = 0; i < stocks.length; i++){
            result =+ stocks[i];
        }

        // 출력
        System.out.println("合計在庫数：" + result);
    }
}
