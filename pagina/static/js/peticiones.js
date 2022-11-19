
var insert_user = () => {
    event.preventDefault();
    let nombre = $('#nombre').val()
    let apellido = $('#apellido').val()
    let identificacion = $('#identificacion').val()
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/insert_user",
        data: JSON.stringify({
            "nombre": nombre,
            "apellido": apellido,
            "identificacion": identificacion,
        })
        ,
        success: function(response){
            alert(response["Mensaje"]);
        },
        error: function (error) {
            console.log(error)  
        }
    })
}

var get_users = () => {
   let id= document.getElementById("id")
   let nombre = document.getElementById("nombre")
   let apellido = document.getElementById("apellido")
   let identificacion = document.getElementById("identificacion")
    event.preventDefault();
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/get_user",
        success: function(response){
            for (var i in response) {
                id.innerHTML+=""+response[i]["id"] +"<br>"
                nombre.innerHTML+=""+response[i]["nombre"]+"<br>"
                apellido.innerHTML+=""+response[i]["apellido"]+"<br>"
                identificacion.innerHTML+=""+response[i]["identificacion"]+"<br>"
            }
        },
        error: function (error) {
            console.log(error)  
        }
    })
}