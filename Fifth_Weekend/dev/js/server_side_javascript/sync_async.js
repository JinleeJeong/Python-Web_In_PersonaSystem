var fs = require('fs');
// Sync
console.log(1);
var data = fs.readFileSync('data.txt', {encoding: 'utf8'});
console.log(data);

// Async
console.log(2);
var data2 = fs.readFile('data.txt', {encoding:'utf8'}, (err, data) => 
{
    console.log(3);
    if(err) throw err;
    console.log(data);
});
console.log(4);

// readFile을 맡긴 후, 완료되면 return