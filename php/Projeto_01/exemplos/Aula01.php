<!DOCTYPE html>
<html>
<head>
    <title>Formulario</title>
</head>
<body>
    <?php
        if (isset($_GET['acao'])){
            $nome = @$_GET['nome'];
            $email =@$_GET['email'];
            echo $nome;
            echo '<br />';
            echo $email;
        }
    ?>
    <form>
        <input type="text" name="nome" />
        <input type="text" name="email" />
        <input type="submit" name="acao" value="Enviar" />
    </form>
</body>
</html>