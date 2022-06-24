<?php
    $file = $_POST['file'];
    $feedback = "";
    function compress_file($arg) {
        $file = $arg;
        $script = 'C:\\Users\\Estagiario\\Desktop\\Py and PHP\\ilovePDF.py';
        $prompt = 'C:\\Users\\Estagiario\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';
        $start = shell_exec("$prompt $script $file");
        if (!empty($arg)) {
            return 'Compressão Realizada com Sucesso!';
        } else {
            return 'Erro ao Compressar!';
        }
        if ($start != null){
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