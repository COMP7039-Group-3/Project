import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, BehaviorSubject } from "rxjs";
import { Section } from "../interfaces/section";

@Injectable({
  providedIn: "root"
})
export class NewsService {
  private readonly apiNewsBbc = "http://localhost:5000/api/bbc";
  private readonly apiNewsGuardian = "http://localhost:5000/api/guardian";
  private readonly apiNewsReuters = "http://localhost:5000/api/reuters";
  private readonly apiNewsWashington = "http://localhost:5000/api/washington";

  constructor(private http: HttpClient) {}

  public selectedSource$: BehaviorSubject<string> = new BehaviorSubject<string>(
    "bbc"
  );

  public getSectionsBbc(): Observable<Section[]> {
    return this.http.get<Section[]>(this.apiNewsBbc);
  }
  public getSectionsGuardian(): Observable<Section[]> {
    return this.http.get<Section[]>(this.apiNewsGuardian);
  }
  public getSectionsReuters(): Observable<Section[]> {
    return this.http.get<Section[]>(this.apiNewsReuters);
  }
  public getSectionsWashington(): Observable<Section[]> {
    return this.http.get<Section[]>(this.apiNewsWashington);
  }
}
