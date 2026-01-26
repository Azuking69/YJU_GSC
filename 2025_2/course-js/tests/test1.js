function prtName() {
  console.log(this.name);
}

class Student {
  name = "gsc";
  prtInfo = undefined;
}

std1 = new Student();
std1.prtInfo = prtName();

std1.prtInfo();
prtName();
