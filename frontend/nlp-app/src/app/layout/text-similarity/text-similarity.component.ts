import { HttpParams } from "@angular/common/http";
import { Component, OnInit } from "@angular/core";
import { DatabaseService } from "src/app/services/database.service";

@Component({
    selector: 'app-text-similarity',
    templateUrl: './text-similarity.component.html'
})
export class TextSimilarityComponent implements OnInit {
    firstInputText: string = "";
    secondInputText: string = "";
    files: any[] = [];
    firstFile: any;
    secondFile: any;
    textSimilarityCalculated: boolean = false;
    textSimilarity: number = 0;

    constructor(
        private service: DatabaseService
    ) {}

    ngOnInit(): void {
        
    }

    getTootlip(arg: any) {
        return {
          text: `${arg.valueText} %`,
        };
    }
    
    customizeText(arg: any) {
        return `${arg.valueText} %`;
    }

    getTextSimilarity() {
        if (this.firstFile && this.secondFile) {
            const formData = new FormData();
            formData.append('firstFile', this.firstFile);
            formData.append('secondFile', this.secondFile);

            this.service.SetRoute(`get-text-similarity/`);
            this.service.GetDataFromFiles(formData).subscribe((data) => {
                this.textSimilarity = Number(data.result);
                this.textSimilarityCalculated = true;
            });
        } else if (this.firstInputText && this.secondInputText){
            let params = new HttpParams();
            params = params.append('firstInputText', this.firstInputText);
            params = params.append('secondInputText', this.secondInputText);
            
            this.service.SetRoute(`get-text-similarity/`);
            this.service.GetDataFromParams(params).subscribe((data) => {
                this.textSimilarity = Number(data.result);
                this.textSimilarityCalculated = true;
            });
        }

    }

    uploadFile(file: any, progressCallback: any) {

        
    }

    onFirstFileUploaded(e: any) {
        this.firstFile = e.file;
        const reader = new FileReader();
        reader.onload = (e) => {
            if (reader.result != null) {
                const text = reader.result.toString().trim();
                this.firstInputText = text;
            }
        }
        reader.readAsText(this.firstFile);
    }

    onSecondFileUploaded(e: any) {
        this.secondFile = e.file;
        const reader = new FileReader();
        reader.onload = (e) => {
            if (reader.result != null) {
                const text = reader.result.toString().trim();
                this.secondInputText = text;
            }
        }
        reader.readAsText(this.secondFile);
    }

    return() {
        this.firstFile = null;
        this.secondFile = null;
        this.firstInputText = '';
        this.secondInputText = '';
        this.textSimilarity = 0;
        this.textSimilarityCalculated = false;
    }
}