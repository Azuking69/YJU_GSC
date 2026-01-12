// =======================================
// 1. 명시적 형변환 (Explicit Conversion)
// =======================================

console.log("=== 명시적 형변환 ===");

// 문자열 → 숫자
let strNum = "123";
console.log(Number(strNum), "→", typeof Number(strNum)); // 123 → number

// 숫자 → 문자열
let num = 456;
console.log(String(num), "→", typeof String(num)); // "456" → string

// 불리언 → 숫자
console.log(Number(true));   // 1
console.log(Number(false));  // 0

// 숫자 → 불리언
console.log(Boolean(0));     // false
console.log(Boolean(123));   // true

// null / undefined
console.log(Number(null));       // 0
console.log(Number(undefined));  // NaN

// 문자열 숫자 → 불리언
console.log(Boolean("0"));   // true (문자열은 비어있지 않으면 true)
console.log(Boolean(""));    // false


// =======================================›
// 2. 암묵적 형변환 (Implicit Conversion)
// =======================================

console.log("\n=== 암묵적 형변환 ===");

// 덧셈 연산자 (+)
console.log("5" + 1);  // "51"   → 문자열 우선
console.log("5" - 1);  // 4      → 숫자 우선

// 비교 연산자
console.log("5" == 5);   // true  (암묵적 변환)
console.log("5" === 5);  // false (타입까지 비교)

// 불리언 컨텍스트
if ("hello") console.log("문자열은 true로 평가");
if (0) console.log("출력 안 됨 — 0은 false로 평가");

// 논리 연산자
console.log(true + 1);   // 2  (true → 1)
console.log(false + 1);  // 1  (false → 0)

// NaN (Not a Number)
console.log("abc" * 2);  // NaN
console.log(typeof NaN); // "number"
