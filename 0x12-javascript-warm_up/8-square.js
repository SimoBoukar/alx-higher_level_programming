#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const num = Number(process.argv[2]);
  let i = 0;
  while (i < num) {
    console.log('X'.repeat(num));
    i++;
  }
}