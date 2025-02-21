import * as Config from '@/config/config';
import axios, { AxiosInstance } from 'axios';

export const API: AxiosInstance = axios.create({ baseURL: Config.API_BASE_URL });