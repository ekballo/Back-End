<!DOCTYPE html>
<html>
<head>
    <title>Formulario</title>
</head>
<body>
    <?php
        if (isset($_POST['acao'])){
           echo $_POST['numero1'] + $_POST['numero2'];
        }
    ?>
    <form method="post">
        <input type="text" name="numero1" />
        <input type="text" name="numero2" />
        <input type="submit" name="acao" value="Enviar" />
    </form>
</body>
</html>