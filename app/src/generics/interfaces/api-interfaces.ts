import { FilterActions } from "../enums/filter-enums";

export interface Response<T = any> {
  data: T;
  meta: Record<string, any>;
}

export interface Filter {
  column: string;
  value: string | number | boolean;
  action: FilterActions;
}

export interface APIFilter {
  limit?: number;
  filters?: Filter[];
  order?: string;
}