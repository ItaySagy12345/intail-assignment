import { Response } from "generics/interfaces/api-interfaces";
import { Author } from "generics/interfaces/models/author";
import { API } from "services/utils/api";

export async function getAuthor(authorName: string): Promise<Response<Author>> {
  return await API.get(`authors/${authorName}`);
}