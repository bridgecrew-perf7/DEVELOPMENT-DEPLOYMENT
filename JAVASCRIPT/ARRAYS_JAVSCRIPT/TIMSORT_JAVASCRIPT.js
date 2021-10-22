#!/usr/bin/env node

//problem: create cubic time compexity example
//solution: nest two times forEach two times within first forEach

let arr1 = [1,2,3,4]
let arr2 = [1,2,3,4]
let arr3 = [1,2,3,4]

arr1.forEach(() => {
    arr2.forEach(() => {
      arr3.forEach(item => console.log(item));
    });
});
