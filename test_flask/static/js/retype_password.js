function confirm_password(user) {
    console.log("enter retype_password")
    $.post('/retype_password',
        {'username': user, 'password': $('#inputPassword').val()}
    ).done(function (data) {
        console.log(data)
        window.location.href='/login'
    }).fail(function (data) {
        console.log(data)
    });
}

$(document).ready(function () {
    console.log('init')
});
