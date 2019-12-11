import { Component, OnInit } from "@angular/core";
import { BreakpointObserver, Breakpoints } from "@angular/cdk/layout";
import { Observable } from "rxjs";
import { map, shareReplay } from "rxjs/operators";
import { FormGroup, FormBuilder, Validators } from "@angular/forms";
import { NewsService } from "../services/news.service";

@Component({
  selector: "app-nav-bar",
  templateUrl: "./nav-bar.component.html",
  styleUrls: ["./nav-bar.component.scss"]
})
export class NavBarComponent implements OnInit {
  public source: string = "";
  get selectedTitle() {
    switch (this.source) {
      case "bbc":
        return "BBC News";
      case "guardian":
        return "The Guardian";
      case "reuters":
        return "Reuters";
      case "washington":
        return "Washington Post";
    }
    return "";
  }

  formGroup: FormGroup;

  isHandset$: Observable<boolean> = this.breakpointObserver
    .observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  constructor(
    private breakpointObserver: BreakpointObserver,
    private formBuilder: FormBuilder,
    private newsService: NewsService
  ) {}

  ngOnInit(): void {
    this.createForm();

    this.newsService.selectedSource$.subscribe(
      source => (this.source = source)
    );
  }

  createForm() {
    this.formGroup = this.formBuilder.group({
      search: []
    });
  }

  public selectSource(source: string) {
    this.newsService.selectedSource$.next(source);
  }
}
