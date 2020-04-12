/**
 * Given an array of urls,
 * construct a sitemap data structure.
 * Currently O(n^2), is it possible to optimize?
 */
const assert = require('assert');

const urls = [
  '/home/animals/cat',
  '/home/animals/dog',
  '/home/cars/audi/r8',
  '/home/cars/tesla/3',
  '/reports/news',
  '/reports/financials',
]

const sitemap = {};

for (const url of urls) {
  const routes = url.split('/');
  routes.shift();
  
  let parent = sitemap;
  for (const route of routes) {
    if (!parent[route]) {
      parent[route] = {};
    }
    parent = parent[route];
  }
}
                    
assert.deepEqual(sitemap, {
  home: {
    animals: {
      cat: {},
      dog: {},
    },
    cars: {
      audi: {
        r8: {},
      },
      tesla: {
        '3': {},
      },
    },
  },
  reports: {
    news: {},
    financials: {},
  },
});
