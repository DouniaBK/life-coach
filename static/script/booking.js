
function onClickCallback(d, t, id, hours_str) {
    //console.log("onClickCallback", id, hours_str)
    const date = document.getElementById("id_time_0")
    const time = document.getElementById("id_time_1")
    
    date.value = d
    time.value = `${t}:00:00`

    // Color in the clicked element
    // Uncolor all others
    
    var hours = JSON.parse(hours_str)
    
    for (let i_d = 0; i_d < 7; i_d++) {
        for (i_h in hours) {
            i_id = `${i_d}_${hours[i_h]}`

            const elem = document.getElementById(i_id);
            elem.style.backgroundColor = '';
        }
      }

    // Color the element pink
    const elem = document.getElementById(id);
    elem.style.backgroundColor = '#f3b0dc';
}

