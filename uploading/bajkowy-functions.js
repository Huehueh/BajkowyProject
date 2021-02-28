
rfid_await_message = "Przyłóż kartę RFID";

async function ReadRfid()
{
    var rfid_text = document.getElementById("rfid_response");
    rfid_text.value = rfid_await_message;

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
      var response = data.get("rfid_response")
      console.log(response);
      if (response != "" && response != rfid_await_message)
      {
          event.preventDefault();
          loader.style.display = "block";
          sound_name.innerHTML = "";

          let ret = await fetch('/hue/upload_file', {method: "POST", body: data});
          sound_name.innerHTML = await ret.text();
          loader.style.display = "none";
          console.log(ret);
      }
      else
      {
        sound_name.innerHTML = "Niepoprawny numer RFID";
      }
      return false;
    }
}
