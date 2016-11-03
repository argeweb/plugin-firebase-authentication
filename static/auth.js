if (typeof firebase !== "undefined" && typeof firebaseui !== "undefined"){
    (function (firebase, firebaseui) {
        var firebase_currentUid = "";
        var ui = new firebaseui.auth.AuthUI(firebase.auth());
        firebase.auth().onAuthStateChanged(function (user) {
            if (user && user.uid == firebase_currentUid) return;
            document.getElementById('firebase_auth_loading').style.display = 'none';
            document.getElementById('firebase_auth_loaded').style.display = 'block';
            user ? handleSignedInUser(user) : handleSignedOutUser();
        });

        firebase.sendUserInfo = function (user){
            var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
            xmlhttp.open("POST", "/firebase_authentication/sign_in");
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify(user));
        };

        var handleSignedInUser = function (user) {
            document.body.className = document.body.className.replace(" auth_signed_out", "").replace(" auth_signed_in", "").replace(" firebase_auth", "");
            document.body.className += " firebase_auth auth_signed_in"; firebase.sendUserInfo(user);
            var s = document.getElementById('firebase_config').getAttribute('data-callback-signed-in');
            if (typeof window[s] === "function") {
                return window[s](user);
            } else {
                return false;
            }
        };

        var handleSignedOutUser = function () {
            document.body.className = document.body.className.replace(" auth_signed_out", "").replace(" auth_signed_in", "").replace(" firebase_auth", "");
            document.body.className += " firebase_auth auth_signed_out";
            var uiConfig = {};
            eval("uiConfig = " + document.getElementById('firebase_config').textContent);
            ui.start('#firebaseui-auth-container', uiConfig);
            var s = document.getElementById('firebase_config').getAttribute('data-callback-signed-out');
            if (typeof window[s] === "function") {
                window[s]();
            }
        };
        document.addEventListener("DOMContentLoaded", function(event) {
            [].forEach.call(document.getElementsByClassName("btn_firebase_signout"), function (el) {
                el.onclick = function (callback, errorCallback){
                    firebase.auth().signOut().then(function() {
                        firebase.sendUserInfo();
                        if (typeof callback === "function"){
                            callback(error);
                        }
                    }, function(error) {
                        if (typeof errorCallback === "function"){
                            errorCallback(error);
                        }
                    });
                };
            });
        });
    }(firebase, firebaseui));
}
