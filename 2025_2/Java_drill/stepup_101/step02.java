package Java_drill.stepup_101;

public class step02 {
    public static void checkOutOfStock(int[] stocks){
        for (int i = 0; i < stocks.length; i++){
            if (stocks[i] == 0){
                System.out.println("在庫切れあり");
                return;
            }
        }
        System.out.println("在庫切れ無し");
    }

    public static void main(String[] args) {
        int stoks1[] = {10, 5, 3, 0, 8};
        checkOutOfStock(stoks1); // 在庫切れあり

        int stock2[] = {1, 2, 3};
        checkOutOfStock(stock2); // 在庫切れ無し

        int stock3[] = {0, 0, 0};
        checkOutOfStock(stock3); // 在庫切れあり
    }
}