const p = console.log;
const lines = (await Deno.readTextFile("2.in")).trim().split("\n");
// const re = new RegExp('Game (\d+): ((\d+ \w+)+,? ?)+;? ?')
const re1 = /Game (\d+): /;
const colors = ["red", "green", "blue"];
const games = lines.slice(0).map((line) => {
  const arr = re1.exec(line);
  const line2 = line.replace(re1, "");
  const ins = line2.split("; ").map((set) => {
    const s = set.split(", ").map((cube) => cube.split(" "));
    return colors.map((c) => {
      return s.find((e) => e[1] === c) ?? ["0", c];
    });
  }).map((arr) => arr.map((a) => Number(a[0])));
  return [Number(arr[1]), ...ins];
});

const part1 = (req) => {
  const impossible = (set) => {
    return set[0] > req[0] || set[1] > req[1] || set[2] > req[2];
  };
  let ans = 0;
  for (const line of games) {
    const [id, ...sets] = line;
    const count = sets.find((set) => impossible(set));
    if (count === undefined) {
      ans += id;
    }
  }
  p({ part1: ans });
};

const part2 = () => {
  const power = (sets) => {
    return Math.max(...sets.map((s) => s[0])) *
      Math.max(...sets.map((s) => s[1])) *
      Math.max(...sets.map((s) => s[2]));
  };
  const ans = games.map((sets) => power(sets.slice(1))).reduce((a, b) => a + b);
  p({ part2: ans });
};
part1([12, 13, 14]);
part2();
