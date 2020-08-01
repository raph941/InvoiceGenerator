var user = $('#data-store').attr('user');
var auth = "False"
if (user == "AnonymousUser"){
    $('#data-store').attr( "auth", "False" );
    auth = "False"
}
else{
    $('#data-store').attr( "auth", "True" );
    auth = "True"
}


//Login
$('#login_btn').click(function(e){
    e.preventDefault()
    $('#loginModal').modal('show')
})

$('#loginform').submit(function(e){
    e.preventDefault()
    var email     = $('#id_username').val()
    var password  = $('#id_password').val()
    var csrf  = $('#loginform').attr('csrf')

    $.ajax({
        url: window.location.host + "/ajax_login/",
        method: "POST",
        data: {
            'csrfmiddlewaretoken': csrf,
            "email":email,
            "password":password,
        },

        success: function(data){
            console.log(data)
            if (data.message == "invalid") {
                $('.alert__wrapper').html(
                    '<div class="alert alert-danger alert-custom alert-dismissible fade show" role="alert">Incorrect Email/Password, try again<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
                );
                $('#data-store').attr( "auth", "False" );
                auth = "False"
            }
            else{
                $('#loginModal').modal('hide')
                $('.header__link').hide()
                $('.header__link2').show()
                $('#data-store').attr('user')
                $('#data-store').attr( "auth", "True" );
                $('.general-alerts').html(
                    '<div class="alert alert-success alert-dismissible fade show" role="alert">Login Successful<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
                );
                auth = "True"
            }
        }
    })
})

// Signup
$('#signup_btn').click(function(e){
    e.preventDefault()
    $('#signupModal').modal('show')
})



$('.downloadBtn').click(function(e){
    if (auth == "False"){
        e.preventDefault()
        $('#loginModal').modal('show')
    }
})



// console.log('submit');
    // let theForm = document.querySelector('#invoice-form');
    // theForm.submit()