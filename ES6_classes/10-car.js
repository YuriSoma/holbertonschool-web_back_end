export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Use Symbol to store clone method
  static _cloneSymbol = Symbol('clone');

  cloneCar() {
    // Create a new object of the same constructor
    return new this.constructor();
  }
}
