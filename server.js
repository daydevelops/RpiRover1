const express = require('express');
const fs = require('fs');
const hbs = require('hbs');

const app = express();

hbs.registerPartials(__dirname + '/views/partials')
app.use(express.static(__dirname+'/public'));
app.set('view engine','hbs');

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
    res.render('index.hbs');
});

app.listen(3000, () => {
    console.log('listening on port 3000');
})
