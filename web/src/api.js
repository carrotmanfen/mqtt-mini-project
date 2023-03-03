const express = require('express');
const mysql = require('mysql');

const app = express();

const connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    port: "3306",
    password: "",
    database: "network2"
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL database!');
});

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
  });

app.get('/api/data', (req, res) => {
  connection.query('SELECT * FROM sensor_data', (error, results, fields) => {
    if (error) throw error;

    res.json(results);
  });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
