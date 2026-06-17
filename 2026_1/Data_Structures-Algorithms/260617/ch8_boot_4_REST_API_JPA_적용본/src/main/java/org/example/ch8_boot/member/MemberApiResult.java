package org.example.ch8_boot.member;

/*
 * REST API 응답을 담기 위한 간단한 클래스
 *
 * 기존 MVC 방식에서는 컨트롤러가 "sign_up_ok" 같은 HTML 파일 이름을 반환했다.
 * REST API 방식에서는 HTML 파일 이름을 반환하지 않고,
 * 브라우저 또는 프론트엔드 JavaScript에게 JSON 데이터를 반환한다.
 *
 * 예)
 * {
 *   "success": true,
 *   "message": "회원가입에 성공했습니다.",
 *   "memberId": "hong"
 * }
 *
 * 이 클래스는 위와 같은 JSON 모양을 만들기 위해 사용한다.
 */
public class MemberApiResult {

    /*
     * success
     * - 요청 처리 성공 여부
     * - true  : 성공
     * - false : 실패
     */
    private boolean success;

    /*
     * message
     * - 사용자에게 보여줄 안내 문구
     * - 예: "회원가입에 성공했습니다.", "아이디 또는 비밀번호가 올바르지 않습니다."
     */
    private String message;

    /*
     * memberId
     * - 로그인 성공 또는 회원가입 성공 시 어떤 회원인지 알려주기 위한 값
     * - 실패했을 때는 null로 둔다.
     */
    private String memberId;

    public MemberApiResult() {
    }

    public MemberApiResult(boolean success, String message, String memberId) {
        this.success = success;
        this.message = message;
        this.memberId = memberId;
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getMemberId() {
        return memberId;
    }

    public void setMemberId(String memberId) {
        this.memberId = memberId;
    }
}
