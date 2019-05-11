import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PlotGraphServiceService {

  constructor(private http: HttpClient) { }

  getStocks(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5000/GetStocksList');
  }

  PlotChangeInHoldings(param): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5000/PlotChangeInHoldings/'+param);
  }



}
