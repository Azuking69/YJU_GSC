package Java_drill.stepup_101;

public class step01 {
    public static void main(String[] args) {
        // 배열 만들기
        int [] stocks1 = {10, 5, 3, 0, 8};
        printStockSum(stocks1);

        int [] stocks2 = {0, 0, 0};
        printStockSum(stocks2);

        int [] stocks3 = {100};
        printStockSum(stocks3);
    }    
        
    public static void printStockSum(int[] stocks){
        // 요소 더하기
        int sum = 0;

        for (int i = 0; i < stocks.length; i++){
            sum += stocks[i];
        }

        // 출력
        System.out.println(sum);
    }
}