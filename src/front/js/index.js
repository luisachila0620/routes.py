/* eslint-disable */

import "../assets/img/rigo-baby.jpg";
import "../assets/img/4geeks.ico";
//import 'breathecode-dom'; //DOM override to make JS easier to use
import "../style/index.scss";

window.onload = async function() {
  console.log("Hello Rigo from the console!");
  const r = await fetch(
    "https://8080-ecc57a96-5727-4659-b3ca-d85ca746097a.ws-us02.gitpod.io/api/excuse"
  );

  document.querySelector("alert").innerHTML = await r.json();
};
