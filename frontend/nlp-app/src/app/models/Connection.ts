export class Connection {
    private url: string;
  
    constructor() {
      this.url = 'http://localhost:8000/api/'
    }
  
    GetUrl(): string {
      return this.url;
    }
}
  