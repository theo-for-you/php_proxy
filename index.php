


<?php

$my_address = '127.0.0.1';
$my_port = "8882";

$headers = apache_request_headers();

$target = $headers["Host2"];
$id = $headers["Id"];


$remote = stream_socket_client("tcp://".gethostbyname($target).":443");
$user = stream_socket_client("tcp://".$my_address.":".$my_port);
fwrite($user, $id);
stream_set_blocking($remote, false); // Trying to be async
stream_set_blocking($user, false);

$data_rem = "";
$data_user = "";


while(1) {
    $data_rem = fread($remote, 2000); /* If there ANY data (up to len), reads ALL data,
                                        if there NO data, returns NOTHING */
    $data_user = fread($user, 2000);  

    if(strlen($data_rem)) {
        error_log('data_rem');
        fwrite($user, $data_rem);
        $data_rem = "";
    }

    if(strlen($data_user)) {
        error_log('data_user');
        fwrite($remote, $data_user);
        $data_user = "";
    }
}



