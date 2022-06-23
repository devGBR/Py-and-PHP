<?php
    $file = $_POST['file'];
    $feedback = "";
    function compress_file($arg) {
        $file = $arg;
        $script = 'ilovePDF.py';
        $prompt = 'C:\\Windows\\System32\\cmd.exe';
        $start = shell_exec("$prompt $command $file");
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