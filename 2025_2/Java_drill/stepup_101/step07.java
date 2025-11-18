import java.util.ArrayList;

// 商品クラス
class Product {
    private String name;
    private int stock;

    public Product(String name, int stock) {
        this.name = name;
        this.stock = stock;
    }

    public String getName() {
        return name;
    }

    public int getStock() {
        return stock;
    }
}

// 商品検索用ユーティリティクラス
class ProductUtil {

    // 名前で検索するメソッド
    public static void searchByName(ArrayList<Product> products, String keyword) {
        boolean found = false;

        for (int i = 0; i < products.size(); i++) {
            Product p = products.get(i);
            if (p.getName().equals(keyword)) {
                System.out.println(p.getName() + "の在庫の数：" + p.getStock());
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("該当なし");
        }
    }
}

// メインクラス
public class step07 {
    public static void main(String[] args) {
        ArrayList<Product> products = new ArrayList<>();
        products.add(new Product("りんご", 10));
        products.add(new Product("みかん", 5));
        products.add(new Product("バナナ", 3));

        // 実行 01
        ProductUtil.searchByName(products, "みかん");
        // 実行 02
        ProductUtil.searchByName(products, "パイナップル");
    }
}
