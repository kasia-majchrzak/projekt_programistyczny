import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { DatabaseService } from "src/app/services/database.service";

@Component({
    selector: 'app-home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

    constructor(
        private service: DatabaseService,
        private router: Router
    ) {}

    ngOnInit(): void {

    }

    compareTexts() {
        this.router.navigate(['./text-similarity']);
    }

    summarizeText() {
        this.router.navigate(['./text-summary']);
    }

    generateWordCloud() {
        this.router.navigate(['./word-cloud']);
    }
}