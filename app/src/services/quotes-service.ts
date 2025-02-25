import { APIFilter, Response } from "generics/interfaces/api-interfaces";
import { Quote } from "generics/interfaces/models/quote";
import qs from "qs";
import { API } from "services/utils/api";


export async function listQuotes(filter?: APIFilter): Promise<Response<Quote[]>> {
  const queryParams: string = qs.stringify(filter);
  return await API.get(`quotes?${queryParams}`);
}