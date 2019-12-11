import { Component, OnInit } from "@angular/core";
import { NewsService } from "../services/news.service";
import { forkJoin, Observable } from "rxjs";
import { Section } from "../interfaces/section";
import { tap, catchError } from "rxjs/operators";

@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.scss"]
})
export class DashboardComponent implements OnInit {
  public sections: Section[] = [];
  public sectionsBbc: Section[] = [];
  public sectionsGuardian: Section[] = [];
  public sectionsReuters: Section[] = [];
  // public sectionsWashington: Section[] = [];

  get selectedSource() {
    return this.newsService.selectedSource$.getValue();
  }
  set selectedSource(source: string) {
    this.newsService.selectedSource$.next(source);
  }

  constructor(private newsService: NewsService) {}

  ngOnInit(): void {
    // this.selectedSource = "bbc";

    this.newsService.selectedSource$.subscribe(source => {
      this.onSourceSelected(source);
    });

    forkJoin([
      this.newsService.getSectionsBbc().pipe(
        tap(sections => {
          this.sectionsBbc = sections;
          this.selectedSource = "bbc";
        }),
        catchError(err => {
          console.warn(`Error scrapping Bbc news`, { err });
          return [];
        })
      ),
      this.newsService.getSectionsGuardian().pipe(
        tap(sections => (this.sectionsGuardian = sections)),
        catchError(err => {
          console.warn(`Error scrapping Guardian news`, { err });
          return [];
        })
      ),
      this.newsService.getSectionsReuters().pipe(
        tap(sections => (this.sectionsReuters = sections)),
        catchError(err => {
          console.warn(`Error scrapping Reuters news`, { err });
          return [];
        })
      )
      // this.newsService.getSectionsWashington().pipe(
      //   tap(
      //     sections => (this.sectionsWashington = sections),
      //     catchError(err => {
      //       console.warn(`Error scrapping Washington news`, { err });
      //       return [];
      //     })
      //   )
      // )
    ])
      .toPromise()
      .then(res => {
        console.log(`All sections for all 4 sources retrieved.`, { res });
      });
  }

  public onSourceSelected(source: string) {
    switch (source) {
      case "bbc":
        this.sections = this.sectionsBbc;
        break;
      case "guardian":
        this.sections = this.sectionsGuardian;
        break;
      case "reuters":
        this.sections = this.sectionsReuters;
        break;
      // case "washington":
      //   this.sections = this.sectionsWashington;
      //   break;

      default:
        break;
    }
  }
}
