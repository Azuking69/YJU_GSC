import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;

// 버튼 클릭 이벤트 처리를 위한 리스너
class MyListener implements ActionListener {
	JTextField jf;
	public MyListener(JTextField j) { // JTextField j = jf;
		jf = j;
	}
	
	@Override // 지워도됨
	public void actionPerformed(ActionEvent e) {
		// 숫자 버튼, 사칙 버튼, clear 버튼, = 버튼 클릭에 대한 처리
		String str = e.getActionCommand(); // 클릭된 버튼 이름 가저오기
		
		switch(str) {
		case "0":	
		case "1":
		case "2":
		case "3":
		case "4":
		case "5":
		case "6":
		case "7":
		case "8":
		case "9":
			
		case "*":
		case "/":
		case "+":
		case "-":
			jf.setText(jf.getText() + str);
			break;
			
		case "=":
			CalLogic c = new CalLogic();
			int result = c.doIt(jf.getText());
			jf.setText(result + "");
			break;
			
		case "C":
			jf.setText("");
			break;
		
			
		}
		
		System.out.println(str);
		if(str.equals("0")) {
			// 숫자 버튼 클릭할 경우 입력창에 숫자가 누적되서 출력되도록~!
			jf.setText("0");
		}else if(str.equals("1")){
			jf.setText("1");
		}		
	}
}

public class CalUI extends JFrame {
	JTextField jf; // 한줄 입력창
	JButton[] b; // 0~9까지 숫자버튼
	JButton clear; // "C" 버튼
	JButton equal; // "=" 바튼
	JButton add, sub, mul, div;	// 시작연산 버튼
	
	
	// class MyInnerListener implements ActionListener{
	// 	@Override
	// 	public void actionPerformed(ActionEvent e) {
	// 		String t = new e.getActionCommand();
	// 		// 내부 믈래스에서는 외부 믈래스 멤버변수 접근이 가능하다.
	// 		jf.setText(t);
	// 	}
	// }
	
	public CalUI() {
		super("계산기"); // 판때기 이름 설정
		FlowLayout layout = new FlowLayout(); // 배치관리자 객체화
		setLayout(layout);  // 판때기에 
		
		jf = new JTextField(15);
		
		// 버튼 클릭 감시자 생성
		MyListener m = new MyListener(jf);
		
		this.add(jf); // 판때기에 입력창 추가
		b = new JButton[10];
		for(int i = 0; i < 10; i++) {
			b[i] = new JButton("" + i);
			this.add(b[i]); // 판때기에 숫자버튼 추가
			b[i].addActionListener(m); // 숫자버튼에 감시자
		}
		
		
		
		// 연산자 버튼
		add = new JButton("+");
		sub = new JButton("-");
		mul = new JButton("*");
		div = new JButton("/");
		equal = new JButton("=");
		
		add(add);
		add(sub);
		add(mul);
		add(div);
		add(equal);
		
		add.addActionListener(m);
		sub.addActionListener(m);
		mul.addActionListener(m);
		div.addActionListener(m);
		equal.addActionListener(m);
		
		// "C" 버튼
		clear = new JButton("C");
		add(clear);
		clear.addActionListener(m);
		clear.setBackground(Color.red);
		
			
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(350, 350);
		setLocation(250, 250);
		setVisible(true);
		
	}
}