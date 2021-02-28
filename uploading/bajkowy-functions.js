

async function ReadRfid()
{
    var rfid_text = document.getElementById("rfid_response");
    rfid_text.value = "Przyłóż kartę RFID";

    let r = await fetch('hue/read_rfid', {method: "GET"});
    rfid_text.value = await r.text();
    console.log(r);
}

window.onload = async function() {
  var form = document.getElementById("soundForm");
  var loader = document.getElementById("loader");
  var sound_name = document.getElementById("sound_name");
  loader.style.display = "none";

  form.onsubmit = async function(event) {
      var data = new FormData(form);
      event.preventDefault();
      loader.style.display = "block";
      sound_name.innerHTML = "";

      let ret = await fetch('/hue/upload_file', {method: "POST", body: data});
      sound_name.innerHTML = await ret.text();
      loader.style.display = "none";
      console.log(ret);

      return false;
    }
}
