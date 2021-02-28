

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
  var loader = document.getElementById("loader")
  loader.style.display = "none";
  form.onsubmit = async function(event) {
      event.preventDefault();
      var data = new FormData(form)
      loader.style.display = "block";
      let ret = await fetch('/hue/upload_file', {method: "POST", body: data});
      var sound_name = document.getElementById("sound_name");
      sound_name.innerHTML = await ret.text();
      loader.style.display = "none";
      console.log(ret);
      return false;
    }
}
