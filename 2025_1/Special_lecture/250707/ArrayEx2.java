
public class ArrayEx2 {

	public static void main(String[] args) {
		// 다차원 배열
		int[][] x = new int[2][2];
		x[0][0] = 10;
		x[0][1] = 20;
		x[1][0] = 30;
		x[1][1] = 40;
		
		int[][] y = {{10, 20}, {30, 40}};
		
		// 다차원 배열에 동적할당
		int[][] k = new int[2][];
		k[0] = new int[3];
		k[1] = new int[2];
		k[0][0] = 10;
		k[0][1] = 20;
		k[1][0] = 30;
		
		k[1][0] = 10;
		k[1][1] = 20;
	}

}
