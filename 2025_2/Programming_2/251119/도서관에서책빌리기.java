

// 학생이 도서관에서 책을 빌리는 기능을 구현하다고 샌각하고
// 관련 믈래스외 메소드를 정의후에 사용

// 책 빌리기
class 학생{
	public void 학생이도서관에서책빌리기(도서관 lib){
		// 학생 방문
		System.out.println("학생: 책을 빌리러 왔습니다.");
		
		// 순서대로 확인
		for(int i = 0; i < lib.books.length; i++){
			// 책이 있는지 확인
			if (lib.books[i] != null) {
				책 b = lib.books[i];
				// 출력
				System.out.println("학생" + b.title + "를 빌렸습니다.");
				
				// 빌렸으니 책장을 비움
				lib.books[i] = null;
				return;
			}
		}
		// 책 없을 때 오류문 출력
		System.out.println("학생: 책이 아무것도 없어요.");
		
	}
}


// 책이 있는 공간
class 도서관{
	// 책 박스 작성(class도 데이터가 됨)
	책[] books;
	// 도서관 크기 결정
	도서관(){
		books = new 책[3];
	}
	
	// 책 입력
	void 초시책등록() {
		books[0] = new 책("ハリー・ポッター", "J.K.ローリング");
		books[1] = new 책("나는 나로 살기로 했다", "김수현");
		books[2] = new 책("아몬드", "손원평");
	}
}


// 책 만들기(이름 없이) -> 위에서 다시 활용하기 때문에 class 만들기
class 책{
	// 그냥 책
	String title;
	// 그녕 저서(같은 이름의 책이 있는지 모르니까 자세히 구분할 수 있도록)
	String author;
	// String title, String author에 이름을 입력
	책(String title, String author){
		this.title = title;
		this.author = author;
	}
}


// 실행
public class 도서관에서책빌리기 {
	public static void main(String[] args) {		
		학생 s = new 학생();
		s.학생이도서관에서책빌리기();
	}
}