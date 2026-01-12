// 1. string (문자열)
const name = "YC Jung";
console.log("name:", name, "→", typeof name);

// 2. number (숫자)
const score = 99.5;
console.log("score:", score, "→", typeof score);

// 3. bigint (큰 정수)
const bigValue = 9007199254740991n;  // 끝에 n을 붙임
console.log("bigValue:", bigValue, "→", typeof bigValue);

// 4. boolean (논리형)
const isPassed = true;
console.log("isPassed:", isPassed, "→", typeof isPassed);

// 5. undefined (값이 정의되지 않음)
let x;
console.log("x:", x, "→", typeof x);

// 6. null (명시적 비어 있음)
const y = null;
console.log("y:", y, "→", typeof y); 
// 'object'로 표시되는 JS 버그 존재

// 7. symbol (고유한 식별자)
const id = Symbol("studentId");
console.log("id:", id, "→", typeof id);


