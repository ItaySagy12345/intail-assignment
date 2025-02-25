import _ from 'lodash';

export function convertSnakeToCamel(snakeObject: Record<string, any>): Record<string, any> {
  if (_.isArray(snakeObject)) {
    return snakeObject.map(convertSnakeToCamel);
  } else if (_.isObject(snakeObject) && snakeObject !== null) {
    return _.mapValues(_.mapKeys(snakeObject, (value, key) => _.camelCase(key)), convertSnakeToCamel);
  }
  return snakeObject;
}