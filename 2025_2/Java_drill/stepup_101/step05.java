public class step05 {  
    public class Product{
        String name;
        int count;

        public Product(String name, int count){
            this.name = name;
            this.count = count;
        }

        public String getName(){
            return name;
        }
        public int getCount(){
            return count;
        }
    }
    
    public static void main(String[] args) {
        Product p1 = new Product("りんご", 10);
        Product p2 = new Product("みかん", 5);

       
        System.out.println(p1.getName() + "(在庫: " + p1.getCount() + ")");
        System.out.println(p2.getName() + "(在庫: " + p2.getCount() + ")");
        
    }
}
