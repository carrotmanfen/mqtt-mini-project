const mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  port: "3306",
  password: "",
  database: "network2"
});

con.connect((err) => {
    if (err) throw err;
    console.log('Connected to MySQL database!');

  });

  

  
