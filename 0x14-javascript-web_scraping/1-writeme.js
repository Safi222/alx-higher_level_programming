#!/user/bin/node
const fs = require('fs');
const path = process.argv[2];
const dest = process.arg[3];
fs.write(path, dest, 'utf8', function (error) {
	if error {
		console.log(error);
	}
});

