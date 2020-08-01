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
            }
            else{
                $('#loginModal').modal('hide')
                $('.header__link').hide()
                $('.header__link2').show()
            }
        }
    })
})

// Signup
$('#signup_btn').click(function(e){
    e.preventDefault()
    $('#signupModal').modal('show')
})


// $('#downloadBtn').click(function(e){
//     e.preventDefault()
//     let user = $('#data-store').attr('user')
//     console.log(user)
//     if (user == "AnonymousUser"){
//         $('#loginModal').modal('show')
//     }
//     else(
//         console.log('submit'),
//         $('#invoice-form').trigger( "submit" )
//     )
// })
