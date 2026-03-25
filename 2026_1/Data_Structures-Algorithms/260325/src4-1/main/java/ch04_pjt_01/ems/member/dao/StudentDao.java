package ch04_pjt_01.ems.member.dao;

// HashMap: DB管理
import java.util.HashMap;
import java.util.Map;

import ch04_pjt_01.ems.member.Student;

public class StudentDao {
	// 学生を保存する箱を作ってる
	private Map<String, Student> studentDB = new HashMap<String, Student>();

	// PHPと同じ
	public void insert(Student student) {
		studentDB.put(student.getsNum(), student);
	}

	public Student select(String sNum) {
		return studentDB.get(sNum);
	}

	public void update(Student student) {
		studentDB.put(student.getsNum(), student);
	}

	public void delete(String sNum) {
		studentDB.remove(sNum);
	}

	// Map = 「キー → 値」でデータを保存する箱
	public Map<String, Student> getStudentDB() {
		return studentDB;
	}

}