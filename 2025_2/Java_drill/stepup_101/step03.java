package Java_drill.stepup_101;

public class step03 {
    public static void printStockList(String[] name, int[] stocks){
        for(int i = 0; i < name.length; i++){
            System.out.println(name[i] + ":" + stocks[i]);
        }
    }

    public static void main(String[] args) {
        String name1[] = {"りんご", "みかん", "バナナ"};
        int stocks1[] = {10, 5, 3};
        printStockList(name1, stocks1);

        String name2[] = {"メロン", "ぶどう"};
        int stocks2[] = {0, 8};
        printStockList(name2, stocks2);
    }
}
