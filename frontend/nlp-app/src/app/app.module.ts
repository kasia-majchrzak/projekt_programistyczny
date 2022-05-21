import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { MatIconModule } from '@angular/material/icon'
import { AppComponent } from './app.component';
import { HomeComponent } from './layout/home/home.component';
import { TextSimilarityComponent } from './layout/text-similarity/text-similarity.component';
import { TextSummaryComponent } from './layout/text-summary/text-summary.component';
import { WordCloudComponent } from './layout/word-cloud/word-cloud.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavMenuComponent } from './nav-menu/nav-menu.component';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule } from '@angular/forms';
import { DxButtonModule, DxCircularGaugeModule, DxFileUploaderModule } from 'devextreme-angular';

const routes: Routes = [
  { path: "", component: HomeComponent },
  { path: "text-similarity", component: TextSimilarityComponent },
  { path: "text-summary", component: TextSummaryComponent },
  { path: "word-cloud", component: WordCloudComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    TextSimilarityComponent,
    TextSummaryComponent,
    WordCloudComponent,
    NavMenuComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    HttpClientModule,
    MatIconModule,
    BrowserAnimationsModule,
    MatButtonModule,
    FormsModule,
    DxFileUploaderModule,
    DxButtonModule,
    DxCircularGaugeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
