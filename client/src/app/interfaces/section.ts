import { NewsUrl as Article } from "./news-url";

export interface Section {
  section: string;
  articles: Article[];
}
