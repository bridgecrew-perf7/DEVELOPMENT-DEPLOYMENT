# Big O Notation Cheat Sheet Javascript

Constant time: O(1)
```javascript
const = arr1 ["one", "two"];
arr1.push("three");
```
```javascript
console.log(arr1.indexOf("three"))
```
```javascript
function findMin(n) {
  let min;
  for(let i = 0; i < n.length; i++) {
    if(min === undefined || min n[i]) {
      min = n[i];
    }
  }
  return min;
};
```
Logarithmic Time: O(log(n))
```javascript
const sort = arr => {
  if (arr1.length < 2) return arr;

  let pivot = arr[0];
  let left = [];
  let right = [];

  for (let i = 1, total = arr1.length; i < total; i++) {
    if (arr1[i] < pivot) left.push(arr[i]);
    else right.push(arr[i]);
  };
  return [
    ...sort(left),
    pivot,
    ...sort(right)
  ];
};
```
Linear Time: O(n)
```javascript
for (let i = 0; i < arr1.length; i++) {
  output += item[i];
  console.log(output);
}
```
```javascript
arr1.forEach(item => console.log(item));
```
Linearithmic Time: O(nlog(n))
```javascript
arr1.forEach(item => console.log(sort(item));
```
Quadratic Time: O(n²)
```javascript
arr1.forEach(() => {
    arr2.forEach(item => console.log(item));
});
```
Cubic Time: O(n³)
```javascript
arr1.forEach(() => {
    arr2.forEach(() => {
      arr3.forEach(item => console.log(item));
    });
});
```
Exponential Time: O(b^n), b > 1
```javascript

```
Factorial Time: O(n!)
```javascript
const factorial = n => {
  let num = n;

  if (n === 0) return 1
  for (let i = 0; i < n; i++) {
    num = n * factorial(n - 1);
  };

  return num;
};

```
