import { HttpParams } from "@angular/common/http";
import { Component, OnInit } from "@angular/core";
import { DatabaseService } from "src/app/services/database.service";
import * as FileSaver from 'file-saver';

@Component({
    selector: 'app-text-summary',
    templateUrl: './text-summary.component.html'
})
export class TextSummaryComponent implements OnInit {
    inputText: string = "";
    files: any[] = [];
    file: any;
    textSummaryGenerated: boolean = false;
    summary: string = "";

    constructor(
        private service: DatabaseService
    ) {}

    ngOnInit(): void {
        
    }

    getTextSummary() {
        if (this.file) {
            const formData = new FormData();
            formData.append('file', this.file);

            this.service.SetRoute(`get-text-summary/`);
            this.service.GetDataFromFiles(formData).subscribe((data) => {
                this.summary = data.result;
                this.textSummaryGenerated = true;
            });
        } else {
            let params = new HttpParams();
            params = params.append('inputText', this.inputText);
            
            this.service.SetRoute(`get-text-summary/`);
            this.service.GetDataFromParams(params).subscribe((data) => {
                this.summary = data.result;
                this.textSummaryGenerated = true;
            });
        }
    }

    return() {
        this.file = null;
        this.inputText = '';
        this.textSummaryGenerated = false;
    }

    download() {
        var blob = new Blob([this.summary], {type: 'text/plain'});
        FileSaver.saveAs(blob, 'summary.txt');
    }

    uploadFile(file: any, progressCallback: any) {

        
    }

    onUploaded(e: any) {
        this.file = e.file;
        const reader = new FileReader();
        reader.onload = (e) => {
            if (reader.result != null) {
                const text = reader.result.toString().trim();
                this.inputText = text;
            }
        }
        reader.readAsText(this.file);
    }
}