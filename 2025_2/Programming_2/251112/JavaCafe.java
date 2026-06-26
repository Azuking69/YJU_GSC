// ☕ レシピ帳（クラス定義）
class Drink {
    String name;
    int price;

    // コンストラクタ（作るときに名前と価格を設定）
    public Drink(String name, int price) {
        this.name = name;
        this.price = price;
    }

    // 作り方（メソッド）
    public void serve() {
        System.out.println(name + " をお出しします。");
    }
}

// 🍵 派生レシピ（継承：Drinkを基にした特製メニュー）
class Latte extends Drink {
    String milkType;

    // super()で親クラスのコンストラクタを呼び出す
    public Latte(String milkType) {
        super("カフェラテ", 450);
        this.milkType = milkType;
    }

    // オーバーライド（親のメソッドを上書き）
    @Override
    public void serve() {
        System.out.println("☕ " + milkType + " ミルクの " + name + " を提供します。");
    }
}

// 📄 契約（interface）
// 全ドリンクに「レシピを表示する」ルールを強制
interface Recipe {
    void showRecipe();
}

// 🧊 冷蔵庫（材料一覧）を管理するクラス
class Fridge {
    String[] items = {"コーヒー豆", "ミルク", "砂糖", "氷"};

    public void showItems() {
        System.out.println("🧊 冷蔵庫の中身：");
        for (String i : items) {
            System.out.println("- " + i);
        }
    }
}

// 👩‍🍳 バリスタ（スタッフ）
// Threadクラスを使って「同時作業」を再現
class Barista extends Thread {
    String name;
    Drink drink;

    public Barista(String name, Drink drink) {
        this.name = name;
        this.drink = drink;
    }

    @Override
    public void run() {
        System.out.println("👩‍🍳 " + name + " が " + drink.name + " を作り始めました。");
        try {
            Thread.sleep(1000); // 作業時間のシミュレーション
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        drink.serve();
        System.out.println("✅ " + name + " の作業完了\n");
    }
}

// ☎ サーバ（注文を受ける役）
class Server {
    public void takeOrder(String customer, Drink d) {
        System.out.println("☎ サーバ：「" + customer + " さんの注文を受け付けました → " + d.name + "」");
    }
}

// 🧍 クライアント（お客さん）
class Customer {
    String name;

    public Customer(String name) {
        this.name = name;
    }

    public void order(Server s, Drink d) {
        System.out.println("🧍 " + name + "：『" + d.name + " ください！』");
        s.takeOrder(name, d);
    }
}

// 🎬 メインプログラム（Javaカフェの入口）
public class JavaCafe {
    public static void main(String[] args) {
        System.out.println("=== ☕ Java Café 開店！ ===\n");

        // 冷蔵庫チェック
        Fridge f = new Fridge();
        f.showItems();
        System.out.println();

        // オブジェクト生成（Drink と Latte）
        Drink coffee = new Drink("アメリカーノ", 400);
        Latte latte = new Latte("オーツ");

        // 客とサーバ
        Customer c1 = new Customer("さき");
        Server s1 = new Server();

        // 注文の流れ
        c1.order(s1, latte);
        c1.order(s1, coffee);
        System.out.println();

        // スタッフが同時に作業開始（スレッド）
        Barista b1 = new Barista("あずき", coffee);
        Barista b2 = new Barista("みるく", latte);

        b1.start();
        b2.start();

        try {
            b1.join();
            b2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("🍽 全ての注文が完了しました。");
    }
}
