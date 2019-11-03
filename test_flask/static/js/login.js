function submit_password() {
    console.log("enter submit_password")
    $.post('/login',
        {'username': $('#inputEmail').val(), 'password': $('#inputPassword').val()}
    ).done(function (data) {
        console.log(data)
        if (data.message.indexOf('successfully') > -1)
        {
            console.log("Successfully login")
            var strs = new Array();
            strs = data.message.split(/[\s\n]/);
            user = strs[4]
//            window.location.href='/mainpage'
            document.write("<form id='login' name='login_mainpage' method='post' action='mainpage'>")
            document.write("<input type='hidden' name='login_user' value='$('#inputEmail').val()'>")
            document.write("</form>")
            document.login_mainpage.submit();
        }
        else
        {
            console.log("Fail to confirm password")
        }
    }).fail(function (data) {

    });
}

function register_account() {
    console.log("enter register_account")
    $.post('/register_account',
        {'username': $('#inputEmail').val(), 'password': $('#inputPassword').val()}
    ).done(function (data) {
        console.log(data)
        if (data.message.indexOf('Successfully') > -1)
        {
            console.log("Successfully register")
            var strs = new Array();
            strs = data.message.split(/[\s\n]/);
            user = strs[4]
//            window.location.href='/retype_password/' + user
            document.write("<form id='retype' name='retype_password' method='post' action='retype_password'>")
            document.write("<input type='hidden' name='username' value='" + user + "'>")
            document.write("</form>")
            document.retype_password.submit();
        }
        else
        {
            console.log("Fail to confirm password")
        }
    }).fail(function (data) {

    });
}

$(document).ready(function () {
    console.log('init')
});
