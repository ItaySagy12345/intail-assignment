import * as Config from '@/config/config';
import * as ObjectHelpers from '@/utils/object-helpers';
import axios, { AxiosInstance, AxiosResponse } from 'axios';

export const API: AxiosInstance = axios.create({ baseURL: Config.API_BASE_URL });

API.interceptors.response.use(
  (response: AxiosResponse<any, any>) => {
    return ObjectHelpers.convertSnakeToCamel(response);
  });