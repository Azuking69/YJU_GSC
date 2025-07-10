import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import java.io.OutputStream;

class MyChat extends JFrame {
	JTextField jf;
	String nick = "";
	public MyChat() {
		nick = JOptionPane.showInputDialog("닉네임을 입력해 주세요: ");
		jf = new JTextField(25);
		jf.addActionListener(new MyListener());
		add(jf);
		setSize(500, 300);
		setLocation(100, 100);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	class MyListener implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			try {
			Socket client = new Socket("10.30.14.160", 8888);
			OutputStream os = client.getOutputStream();
			String msg = nick + ":" +  jf.getText();
			os.write(msg.getBytes());
			jf.setText("");
			}catch(Exception ignore) {
			}
		}
	}
}

public class Client {
	public static void main(String args[])
			throws UnknownHostException, IOException{
		new MyChat().setVisible(true);
		}
}

