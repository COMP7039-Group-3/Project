import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Post } from "../interfaces/post";
import { Observable } from "rxjs";
import { Section } from "../interfaces/section";

@Injectable({
  providedIn: "root"
})
export class NewsService {
  private readonly apiUrl = "https://jsonplaceholder.typicode.com/posts";
  private readonly apiNewsBbc = "http://localhost:5000/api/bbc";

  constructor(private http: HttpClient) {}

  public getPosts(): Observable<Post[]> {
    return this.http.get<Post[]>(this.apiUrl);
  }

  public getSectionsBbc(): Observable<Section[]> {
    return this.http.get<Section[]>(this.apiNewsBbc);
  }
}
