const jsSHA = require("jssha");

// ok: jssha-sha1
new jsSHA("SHA-512", "TEXT", { encoding: "UTF8" });
// ruleid: jssha-sha1
new jsSHA("SHA-1", "TEXT", { encoding: "UTF8" });