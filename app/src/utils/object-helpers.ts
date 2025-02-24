import { camelCase, mapKeys } from 'lodash';

export function convertSnakeToCamel(object: any): any {
  return mapKeys(object, (_, key) => camelCase(key));
}