import { Component, OnInit } from '@angular/core';
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'nlp-app'; 

  constructor(
    private matIconRegistry: MatIconRegistry, 
    private sanitizer: DomSanitizer
  ) {}

  ngOnInit(): void {
    
  }

  loadIcons() {
    this.matIconRegistry.addSvgIcon('home', '../assets/icons/home_FILL1_wght400_GRAD0_opsz24.svg');
    this.matIconRegistry.addSvgIcon('cloud', '../assets/icons/cloud_FILL1_wght400_GRAD0_opsz24.svg');
    this.matIconRegistry.addSvgIcon('content_paste_search', '../assets/icons/content_paste_search_FILL1_wght400_GRAD0_opsz24.svg');
    this.matIconRegistry.addSvgIcon('edit_note', '../assets/icons/edit_note_FILL1_wght400_GRAD0_opsz24.svg');
  }

}
