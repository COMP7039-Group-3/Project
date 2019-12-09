import { Component, OnInit } from "@angular/core";
import { map } from "rxjs/operators";
import { Breakpoints, BreakpointObserver } from "@angular/cdk/layout";
import { NewsService } from "../services/news.service";

@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.scss"]
})
export class DashboardComponent {
  public posts$ = this.newsService.getPosts();

  public sections$ = this.newsService.getSectionsBbc();

  constructor(private newsService: NewsService) {}
}
