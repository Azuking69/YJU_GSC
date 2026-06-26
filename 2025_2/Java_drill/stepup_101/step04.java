package Java_drill.stepup_101;

import java.util.ArrayList;

public class step04 {
    public static void convertAndPrintList(String[] names){
        ArrayList<String> list = new ArrayList<>();

        for (int i = 0; i < names.length; i++){
            list.add(names[i]);
        }

        for (int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }
    }

    public static void main(String[] args) {
        String names1[] = {"りんご", "みかん", "バナナ"};
        convertAndPrintList(names1);

        String names2[] = {"メロン", "ぶどう"};
        convertAndPrintList(names2);
    }
}