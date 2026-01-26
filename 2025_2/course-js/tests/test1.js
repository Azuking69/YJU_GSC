class Car {
  model = undefined;
  prtModel = undefined;
  constructor(argModel) {
    this.model = argModel;
  }
  prtModel() {
    console.log(this.model);
  }
}

class enCar {
  prtList = undefined;
}

car1 = new Car("Y");
car1.prtModel(); // 출력: Y
// car1.prtModel = enCar;

// car1.prtModel(); // 출력: Y
// enCar(); // 출력: undefined

const encar = car1.prtModel;
encar();
