

async function ReadRfid()
{
    var rfid_text = document.getElementById("rfid_response");
    rfid_text.value = "Przyłóż kartę RFID";

    let r = await fetch('hue/read_rfid', {method: "GET"});
    rfid_text.value = await r.text();
    console.log(r);
}

window.onload = async function() {
  form = document.getElementById("soundForm");
  form.onsubmit = async function(event) {
      event.preventDefault();
      var data = new FormData(form)
      let ret = await fetch('/hue/upload_file', {method: "POST", body: data});
      rfid_text.value = await r.text();
      console.log(r);
      return false;
    }
}
