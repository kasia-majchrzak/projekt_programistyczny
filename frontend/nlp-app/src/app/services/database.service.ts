import { Injectable } from "@angular/core";
import { Connection } from "../models/Connection";
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { environment } from "../../environments/environment";
import { Observable } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class DatabaseService {
  connection: Connection;
  route: string = '';
  json = 'json/';

  constructor(private http: HttpClient) {
    this.connection = new Connection();
  }

  SetRoute(_path: string) {
    this.route = this.connection.GetUrl() + _path;
  }

  AddObj<T>(_obj: any): Observable<T> {
    return this.http.post<T>(this.route, _obj);
  }

  GetDataFromParams(params: HttpParams): Observable<any> {
    return this.http.get(this.route, { params: params });
  }

  GetDataFromFiles(formData: FormData): Observable<any> {
    let headers = new HttpHeaders();
    headers = headers.append('Content-Type','multipart/form-data');

    return this.http.post(this.route, formData);
  }

  GetFileFromFiles(formData: FormData): Observable<any> {
    let headers = new HttpHeaders();
    headers = headers.append('Content-Type','multipart/form-data');

    return this.http.post(this.route, formData, { responseType: 'arraybuffer' });
  }

  GetFileFromParams(params: HttpParams): Observable<any> {
    let headers = new HttpHeaders();
    headers = headers.append('Content-Type','multipart/form-data');

    return this.http.get(this.route, { params: params, responseType: 'arraybuffer' });
  }

  UpdateObj<T>(_obj: any): Observable<T> {
    return this.http.put<T>(this.route + `/${_obj.id}`, _obj);
  }

  Update<T>(_obj: any): Observable<T> {
    return this.http.put<T>(this.route, _obj);
  }

  DeleteObj<T>(_obj: any): Observable<any> {
    return this.http.delete<T>(this.route + `/${_obj.id}`);
  }

  Delete<T>(): Observable<any> {
    return this.http.delete<T>(this.route);
  }
}
