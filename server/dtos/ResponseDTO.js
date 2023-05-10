export class ResponseDTO {
  constructor(status, message, data = undefined) {
    this.status = status;
    this.message = message;
    this.data = data;
  }
}
