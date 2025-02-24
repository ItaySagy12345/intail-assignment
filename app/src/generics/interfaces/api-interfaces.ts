export interface Response<T = any> {
  data: T;
  meta: Record<string, any>;
}

export interface APIFilter {
  page: number;
  size: number;
}