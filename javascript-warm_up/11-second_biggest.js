#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let first = -Infinity;
  let second = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > first) {
      second = first;
      first = args[i];
    } else if (args[i] > second && args[i] < first) {
      second = args[i];
    }
  }

  if (second === -Infinity) {
    console.log(0);
  } else {
    console.log(second);
  }
}
