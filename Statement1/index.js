const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const Student = require("./models");
const dbConfig = require("./config");

const app = express();
app.set("view engine","ejs");
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

mongoose.connec(dbConfig.url,{
    useNewUrlParser: true,
})
.then(() => {
    console.log("Successfully connected to the database");
}).catch((err) => {
    console.log("could not connect to database",err);
    process.exit();
})

app.use("/css", express.static(path.resolve(__dirname, "static/css")));
app.get("/", (req, res) => {
  res.render("index");
});

app.post("/addmarks",(req,res) => {
    var myData = new Student(req.body);
    myData.save()
    .then((item) => {
        console.log("item saved Successfully");
        res.redirect("/getMarks");
    })
    .catch((err)=>{
        res.status(400).send("unable to save to database");
    });
})

