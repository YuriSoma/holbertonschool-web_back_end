export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Getters & Setters
  get code() {
    return this._code;
  }

  set code(newCode) {
    this._code = newCode;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = newName;
  }

  // Method
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
