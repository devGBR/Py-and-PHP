<?php
    $file = $_POST['file'];
    $feedback = "";
    function compress_file($arg) {
        $command = escapeshellcmd("script.py");  
        $start = shell_exec($command);
        if (!empty($start)) {
            return 'Compressão Realizada com Sucesso!';
        } else {
            return 'Erro ao Compressar!';
        }
    }

    if($file != null) {
        $feedback = compress_file($file);
    }
?>
<DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>
        Anexar arquivo
    </title>
</head>
<body>
    <p> <?php echo $feedback; ?> </p>
    <p> <?php echo $file; ?> </p>
</body>
</html>