import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { PlotGraphServiceService } from './plot-graph-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'my-stock-app';
  fromDate: any;
  toDate: any;
  imageUrl: any;
  stock: any;
  isImageLoaded: boolean = false;
  stocks = [];
  isLoaded = false;
 isImageBeingLoaded =false; 
  constructor(private plotGraphServiceService:PlotGraphServiceService){
   
  }

  ngOnInit() {
    this.plotGraphServiceService.getStocks().subscribe((stocks) => {
          this.stocks = stocks;
      this.isLoaded = true;
    });
  }

  plotShareHolding() {
    let param;    this.isImageBeingLoaded =true;
    let startDateParam = this.fromDate.year + '-' + this.fromDate.month + '-' + this.fromDate.day;
    let endDateParam = this.toDate.year + '-' + this.toDate.month + '-' + this.toDate.day;
    param = startDateParam + '/' + endDateParam + '/' + this.stock;
    this.plotGraphServiceService.PlotChangeInHoldings(param).subscribe((imageUrl) => {
      this.imageUrl = 'data:image/jpg;base64,'+imageUrl;
      this.isImageLoaded = true;
	this.isImageBeingLoaded =false;
    },
      error => {
 	this.imageUrl = 'data:image/png;base64,'+ error.error.text
      	this.isImageLoaded = true;
	 this.isImageBeingLoaded =false;
      });
  }

   
}
