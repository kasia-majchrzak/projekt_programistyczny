import { HttpParams } from "@angular/common/http";
import { Component, OnInit } from "@angular/core";
import { DomSanitizer } from "@angular/platform-browser";
import { DatabaseService } from "src/app/services/database.service";
import * as FileSaver from 'file-saver';

@Component({
    selector: 'app-word-cloud',
    templateUrl: './word-cloud.component.html'
})
export class WordCloudComponent implements OnInit {
    inputText: string = "";
    files: any[] = [];
    file: any;
    wordCloudGenerated: boolean = false;
    image: any;
    imageBlob: any;

    constructor(
        private service: DatabaseService, 
        private sanitizer: DomSanitizer
    ) {}

    
    ngOnInit(): void {
        
    }

    getWordCloud() {        
        if (this.file) {
            const formData = new FormData();
            formData.append('file', this.file);

            this.service.SetRoute(`get-word-cloud/`);
            this.service.GetFileFromFiles(formData).subscribe((data) => {
                const blob = new Blob([data] , {type:'image/*'});
                this.imageBlob = URL.createObjectURL(blob);
                this.image = this.sanitizer.bypassSecurityTrustUrl(this.imageBlob);
                this.wordCloudGenerated = true;
            });
        } else if (this.inputText) {
            let params = new HttpParams();
            params = params.append('inputText', this.inputText);
            
            this.service.SetRoute(`get-word-cloud/`);
            this.service.GetFileFromParams(params).subscribe((data) => {
                const blob = new Blob([data] , {type:'image/*'});
                this.imageBlob = URL.createObjectURL(blob);
                this.image = this.sanitizer.bypassSecurityTrustUrl(this.imageBlob);
                this.wordCloudGenerated = true;
            });
        }
    }

    download() {
        FileSaver.saveAs(this.imageBlob, 'wordcloud.jpg');
    }

    return() {
        this.inputText = '';
        this.file = null;
        this.image = null;
        this.wordCloudGenerated = false;
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