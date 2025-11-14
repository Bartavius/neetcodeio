const map1 = new Map();
map1.set('key1', 'value1');
map1.set('key2', 'value2');

const map2 = new Map();
map2.set('key1', 'value1');
map2.set('key2', 'value2');

const map3 = new Map(map2);

console.log(`map1 and map2 type equality: ${map1 == map2}`);
console.log(`map1 and map2 pointer equality: ${map1 === map2}`);
console.log(`map2 and map3 pointer equality: ${map1 === map2}`);
console.log(`accessing an element that doesn't exist: ${map1['key2'] ?? 0}`);