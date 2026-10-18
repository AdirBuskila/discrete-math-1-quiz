// dumps the relations level files as JSON on stdout
const fs = require("fs"), path = require("path");
const dir = path.join(__dirname, "..", "..", "..", "..", "courses", "relations");
const out = {};
for (const f of fs.readdirSync(dir).filter(f => /^C\d+\.js$/.test(f)).sort()) {
  const src = fs.readFileSync(path.join(dir, f), "utf8");
  new Function("COURSE_LEVEL", src)((id, lv) => { out[lv.id] = lv; });
}
process.stdout.write(JSON.stringify(out));
