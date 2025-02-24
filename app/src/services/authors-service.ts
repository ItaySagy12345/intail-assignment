import { API } from "@/services/utils/api";
import { Response } from "@/generics/interfaces/api-interfaces";
import { Author } from "@/generics/interfaces/models/author";

export async function getAuthor(authorName: string): Promise<Response<Author>> {
  return await API.get(`authors/${authorName}`);
}