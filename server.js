const express = require('express');
const fs = require('fs');

const app = express();

app.use((req,res,next) => {
    var now = new Date().toString();
    var log = now + ' ' + req.method + ' ' + req.url;
    fs.appendFile('logs/access.log',log+ '\n', (err) => {
        if (err) {
            console.log(err);
        }
    });
    next();
})

app.get('/',(req,res) => {
    res.send('Hello Wrold');
});

app.listen(3000, () => {
    console.log('listening on port 3000');
})
