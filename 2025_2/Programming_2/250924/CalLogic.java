import java.util.StringTokenizer;

public class CalLogic {
	// 계산식을 파라미터로 남겨주면 계산결과를 리턴하는 메소드 구현
	public int doIt(String str){
		int result = 0;
	
		StringTokenizer t = new StringTokenizer(str, "+-*/", true);
		while(t.hasMoreElements()){ // 더 가져울 토큰이 있다면
			String r = t.nextToken();
			// Integer.parseInt("0"); => 문자형 -> int 형으로 변경
			// result = result + Integer.parseInt(r);  
			
			if (r.equals("+")){
				//연산자(r)가(.equals()) 덧셈이라면("+")
				//덧셈
				result = result + Integer.parseInt(t.nextToken());
			}else if(r.equals("-")){
				//연산자(r)가(.equals()) 뺄셈이라면("-")
				//뺄셈
				result = result - Integer.parseInt(t.nextToken());
			}else if(r.equals("*")){
				//연산자(r)가(.equals()) 곱셈이란면("*")
				//곱셈
				result = result * Integer.parseInt(t.nextToken());
			}else if(r.equals("/")){ 
				//(연산자(r)가(.equals()) 나눗셈이란면("/")
				//나눗셈
				result = result / Integer.parseInt(t.nextToken());
			}else { 
				// r이 "+-*/" 아니라면 남은건 숫자
				result = Integer.parseInt(r); // r 숫자형으로 바꿔서 저장
			}
		}		
		return result;
	}
}