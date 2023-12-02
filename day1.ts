const p = console.log;

const lines = (await Deno.readTextFile("1.in")).trim().split("\n");

const numRE = new RegExp("[0-9]");
const part1 = (lines) => {
  const ans = lines.map((line) => {
    const numbers = line.split("").filter((c) => numRE.test(c));
    // p({line, numbers, makes: Number(numbers[0] + numbers[numbers.length - 1])})
    return numbers;
  }).map((arr) => Number(arr[0] + arr[arr.length - 1]))
    // .map(c => {p(c); return c})
    .reduce((a, b) => a + b);
  p({ part1: ans });
};

const numwords = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
];
const part2 = (lines) => {
  const ans = lines.map((line) => {
    const numbers = [];
    for (let i = 0; i < line.length; i++) {
      if (numRE.test(line[i])) {
        numbers.push(line[i]);
      } else {
        for (let j = 1; j < numwords.length; j++) {
          const word = numwords[j];
          if (line.slice(i).startsWith(word)) {
            numbers.push("" + j);
          }
        }
      }
    }
    return numbers;
  }).map((arr) => Number(arr[0] + arr[arr.length - 1]))
    .reduce((a, b) => a + b);
  p({ part2: ans });
};

// part1(lines)
part2(lines);
