
// 접근 제한자
// private - default - protected - public
//           package   package
//　private : 同じクラスでしか使用可能
//　default : 同じパッケージでしか使用可能
//　protected : 同じパッケージ、違うパッケージでも継承を使えば使用可能
//　public : 誰でもOK

// オブジェクト生成は自由に：同じパッケージでは誰でもオブジェクト生成可能
//class Mysingleton {
//    int count = 0;
//}



// 객체 생성 단 하나만!! 유지되도록 생성
class Mysingleton {
    int count = 0;
    static Mysingleton m ;
    // コンストラクタ　接近制限が、プライベートで宣言されたので
    // 現在のクラス内部へだけ、オブジェクト生成可能
    // 外部へは、オブジェクト生成不可
    private  Mysingleton() {}
    public synchronized static Mysingleton createMysingle(){
        if (m == null) {
            m = new Mysingleton();

        }
        return m;
    }
}

public class Test {
    public static void main(String[] args){
//        Mysingleton m1 = new Mysingleton();
        Mysingleton m1 = Mysingleton.createMysingle();
        System.out.println(m1.count++);
        Mysingleton m2 = Mysingleton.createMysingle();
//        System.out.println(m2.count++);
    }
}