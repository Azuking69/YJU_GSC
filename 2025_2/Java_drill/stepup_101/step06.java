import java.util.ArrayList;

import Java_drill.stepup_101.step05.Product;

class step06 {
    public class main{
        public static void main(String args[]){
        // 리스트 작성
        ArrayList<Product> products = new ArrayList<>();

        // 제품 추가
        products.add(new Product("사과", 10));
        products.add(new Product("귤", 5));
        products.add(new Product("바나나", 3));

            // 제품 리스트 출력
            for (int i = 0; i < products.size(); i++){
                Product p = products.get(i);
                System.out.println(p.getName() + "(재고: " + p.getStock() + ")");
            }
        }
    }
}

    