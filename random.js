const express = require("express");
const app = express();
app.use(express.urlencoded({ extended: true }));
const bodyParser = require("body-parser");
app.set("view engine", "ejs");
const methodOverride = require("method-override");
app.use(methodOverride("_method"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use("/public", express.static("public"));
var admin = require("firebase-admin");
var serviceAccount = require("./random.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://random-7ef55-default-rtdb.firebaseio.com",
});




const server = app.listen(3001, () => {
  console.log("start server:3001 hi");
});

app.get("/", function (요청, 응답) {
  응답.render("index.ejs");
});


app.get("/hihi", function (요청, 응답) {
  응답.render("voice2.ejs");
});


app.get("/voice2", function (요청, 응답) {
  응답.render("voice2.ejs");
});
var create_image_num=0;
app.post("/voice2", function (요청, 응답) {
  console.log(요청.body.strings);
  const spawn = require("child_process").spawn;
  const result = spawn("Python", ["text2image.py", 요청.body.strings]);
 
  result.stdout.on("data", function (data) {
    console.log(data.toString());
    
   
    const spawn = require("child_process").spawn;
    const result = spawn("Python", ["show_gaugan.py",create_image_num]);
    create_image_num=create_image_num+1;



  });
  result.stderr.on("data", function (data) {
    console.log(data.toString());
  });

  응답.status(200).send({ message: "성공했어용" });

});


app.get("/upload", function (요청, 응답) {
  //console.log('gg');
  응답.render("up.ejs");
});

//삭제요청!!
app.post("/delete", function (요청, 응답) {
  //console.log(요청.body)
  //console.log(요청.body._id.category);

  admin
    .firestore()
    .collection(요청.body._id.category)
    .doc(요청.body._id.imageName)
    .delete()
    .then(() => {
      응답.status(200).send({ message: "성공했어용" });
    });
});

app.post("/apply", function (요청, 응답) {
  //console.log(요청.body.url)

  const spawn = require("child_process").spawn;
  const result = spawn("Python", ["show_image.py", 요청.body.url]);
  result.stdout.on("data", function (data) {
    console.log(data.toString());
    console.log("22");
    console.log(data);
    var datas = "";
    datas += data.toString();
    console.log("33");
    //console.log(datas);
  });
  result.stderr.on("data", function (data) {
    console.log(data.toString());
  });

  응답.status(200).send({ message: "성공했어용" });
});

app.get("/list", function (요청, 응답) {
  var arr = [];
  var n = 0;
  admin
    .firestore()
    .collection("인물")
    .get()
    .then((결과) => {
      결과.forEach((doc) => {
        arr[n] = doc.data();
        n = n + 1;
      });
      for (i = 0; i < n; i++) {
        arr[i].날짜 = new Date(arr[i].날짜.seconds * 1000);
      }
      응답.render("listtest.ejs", { posts: arr });
    });
});

app.get("/list/:type", function (요청, 응답) {
  let { type } = 요청.params;
  var arr = [];
  var n = 0;
  admin
    .firestore()
    .collection(type)
    .get()
    .then((결과) => {
      결과.forEach((doc) => {
        arr[n] = doc.data();
        n = n + 1;
      });
      for (i = 0; i < n; i++) {
        arr[i].날짜 = new Date(arr[i].날짜.seconds * 1000);
      }
      응답.render("listtest.ejs", { posts: arr });
    });
});

app.post("/list", function (요청, 응답) {
  // var name=요청.body.Name;
  console.log(요청.body);
  var arr = [];
  var n = 0;

  admin
    .firestore()
    .collection("인물")
    .where("이미지이름", "==", 요청.body.Name)
    .get()
    .then((결과) => {
      if (결과.empty) {
      } else {
        결과.forEach((doc) => {
          arr[n] = doc.data();
          n = n + 1;
        });
        for (i = 0; i < n; i++) {
          arr[i].날짜 = new Date(arr[i].날짜.seconds * 1000);
        }
      }
      응답.render("listtest.ejs", { posts: arr });
    });

  console.log(arr);
});

app.post("/list/slide", function (요청, 응답) {
  // var name=요청.body.Name;
  //console.log(요청.body)
  var arr = 요청.body.url;
  var n = 0;
  const spawn = require("child_process").spawn;
  const result = spawn("Python", ["slide_show.py", 요청.body.url]);
  result.stdout.on("data", function (data) {
    console.log(data.toString());
  });
  result.stderr.on("data", function (data) {
    console.log(data.toString());
  });

  응답.status(200).send({ message: "성공했어용" });
});




