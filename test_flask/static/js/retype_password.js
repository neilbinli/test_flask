function confirm_password(user) {
    console.log("enter retype_password")
    $.post('/retype-password',
        {'username': user, 'password': $('#inputPassword').val()}
    ).done(function (data) {
        console.log(data)
        // window.location.href='/login'
    }).fail(function (data) {

    });
}

$(document).ready(function () {
    console.log('init')
});
